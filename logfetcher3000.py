import argparse
import datetime
import json
import logging
import os
import re
import requests
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-v', '--verbose', help="Toggle verbose debug logging", action="store_true")
args = parser.parse_args()

error_logger = logging.getLogger()
error_logger.setLevel(logging.ERROR)

output_file_handler = logging.FileHandler("debug.log")
stdout_handler = logging.StreamHandler(sys.stdout)

if args.verbose:
    error_logger.addHandler(output_file_handler)
    error_logger.addHandler(stdout_handler)
else:    
    error_logger.addHandler(output_file_handler)

def get_links_from_file(filename):
    """Read in JSON file containing list of links
       ond convert all characters to lowercase.
       :param filename: string
    """
    try:
        with open(filename) as json_file:
            url_json_object = json.load(json_file)
            # Ensure all dict items are lower case
            url_json_object = {k.lower(): [i.lower() for i in v] for k, v in url_json_object.items()}
    except IOError as e:
        print("An error has occurred: {}".format(e))
        sys.exit()
    return url_json_object
            

def get_log(url, filename):
    """
    Download the log files and save them locally.
    Set User-Agent when accessing websites to LogFetcher3000.
    :param url: list
    :param filename: string
    """
    headers = {'User-Agent': 'LogFetcher3000'}
    r = requests.get(url, allow_redirects=True, headers=headers)
    if r.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(r.content)
    else:
        logging.error("Unexpected HTTP response code received: {}".format(r.status_code))


if __name__ == '__main__':
    links_filename = "links.json"
    if not os.path.exists(links_filename):
        print("An error has ocurred. Cannot find JSON file: {}".format(links_filename))
        sys.exit()
    date_stamp = datetime.datetime.today().strftime('%m%d%Y_%H%M%S')
    url_object = get_links_from_file(links_filename)
    access_links = url_object["access"]
    error_links = url_object["error"]

    for i in range(len(access_links)):
        if access_links[i]:
            if not re.search('^https?://', access_links[i]):
                logging.error("Incorrect protocol used: {}".format(access_links[i]))
                continue # Move on to the next iteration in the loop
            else:
                log_filename = access_links[i].split('/')
                log_filename = log_filename[3]
                get_log(access_links[i], '{}_access_{}.log'.format(log_filename, date_stamp))
    for i in range(len(error_links)):
        if error_links[i]:
            if not re.search('^https?://', error_links[i]):
                logging.error("Incorrect protocol used: {}".format(error_links[i]))
                continue # Move on to the next iteration in the loop
            else:
                log_filename = re.findall('.*account_name=([^&]*)', error_links[i])
                log_filename = log_filename[0]
                get_log(error_links[i], '{}_error_{}.log'.format(log_filename, date_stamp))
