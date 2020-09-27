# About
LogFetcher3000 is a Python based tool to retrieve access and error logs from WP Engine hosted websites that utilize the WP Engine Must Use plugins.

# Usage
This tool uses a JSON file to hold the current access and current error log for the site in question. The current version only handles a single set of links and is in the following format:

```
{"access": "https://mysite.com/link/to/access.log", "error": "https://mysite.com/link/to/error.log"}
```

The links can be obtained from within the `WP Admin Dashboard` within the WPE MU Plugin and inserted in a file called `links.json`.

# Requirements
I haven't currently made a `requirements.txt` file, however `requests` will need to be installed for the script to work.

# Change Log
All notable changes to this project will be documented in this section.

## [0.1] - 2020-09-26
### Added
- Ability to add links to a JSON file to be read by the script
- Automaed filename creation based on the domain used for the access logs
