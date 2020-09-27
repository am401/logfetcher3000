import datetime
import json
import requests

# Generate datestamp uisng date and time in order to create unique file names
d_stamp = datetime.datetime.today()
d_stamp = d_stamp.strftime('%m%d%Y_%H%M%S')

# Set links within a JSON string to be utilized
with open('links.json') as json_file:
    url_json_object = json.load(json_file)


def get_log(url, filename):
    headers = {'User-Agent': 'LogFetcher3000'}
    r = requests.get(url, allow_redirects=True, headers=headers)
    open(filename, 'wb').write(r.content)


if __name__ == '__main__':
    domain = url_json_object["access"].split('/')
    log_filename = domain[2].replace(".", "_")
    get_log(url_json_object["access"], '{}_{}.log'.format(log_filename, d_stamp))
    get_log(url_json_object["error"], '{}_error_{}.log'.format(log_filename, d_stamp))
