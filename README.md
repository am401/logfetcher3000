# About
LogFetcher3000 is a Python based tool to retrieve access and error logs from WP Engine hosted websites that utilize the WP Engine Must Use plugins.

# Usage
This tool uses a JSON file to hold the current access and current error log for the site in question. Links should be added as lists within the dictionary: 

```
{"access": ["https://mysite.com/link/to/access.log"], "error": ["https://mysite.com/link/to/error.log", "https://myothersite.com/link/to/error.log"]}
```

The links can be obtained from within the `WP Admin Dashboard` within the WPE MU Plugin and inserted in a file called `links.json`.

# cron
This script can be called by a cron at a specific time  to download the day's logs. For example to grab the logs on the hour every hour:

```
0 * * * * cd /path/to/logfetcher3000 && /usr/local/bin/python3 logfetcher3000.py
```

# Change Log
All notable changes to this project will be documented in this section.

## [0.2] - 2020-10-22
### Changed
- Set the D_STAMP global variables to uppercase
- Moved opening the JSON file under __main__
- Handling the file under get_log() to be with a content manager
- Generated filenames are now in the format of `environmentname_[access|error]_datestamp.log`
### Added
- Support for dynamically reading each dictionary value by looping through the list provided in `links.json`
- Regex library to get the environment name from error log link
- Created requirements.txt
## [0.1] - 2020-09-26
### Added
- Ability to add links to a JSON file to be read by the script
- Automaed filename creation based on the domain used for the access logs
