import datetime
import json
import re
import requests

# Generate datestamp for unique file names
D_STAMP = datetime.datetime.today()
D_STAMP = D_STAMP.strftime('%m%d%Y_%H%M%S')


def get_log(url, filename):
    """
    Function to download the log files and save them locally.
    Set User-Agent when accessing websites to LogFetcher3000.
    :param url: list
    :param filename: string
    """
    headers = {'User-Agent': 'LogFetcher3000'}
    r = requests.get(url, allow_redirects=True, headers=headers)
    with open(filename, 'wb') as f:
        f.write(r.content)


if __name__ == '__main__':
    with open('links.json') as json_file:
        url_json_object = json.load(json_file)
    access_links = url_json_object["access"]
    error_links = url_json_object["error"]
    """
    Loop through each list under the given key in the dict.
    This allows for scalability of the script.
    Using the if statements in case the dict value is empty.
    """
    for i in range(len(access_links)):
        if access_links[i]:
            log_filename = access_links[i].split('/')
            log_filename = log_filename[3]
            get_log(access_links[i], '{}_access_{}.log'.format(log_filename, D_STAMP))
    for i in range(len(error_links)):
        if error_links[i]:
            log_filename = re.findall('.*account_name=([^&]*)', error_links[i])
            log_filename = log_filename[0]
            get_log(error_links[i], '{}_error_{}.log'.format(log_filename, D_STAMP))
