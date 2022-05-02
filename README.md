# PyBuster

Recreation of the [GoBuster](https://github.com/OJ/gobuster) tool written in Python3.  

Bruteforce tool used to discover Web URIs for websites, Vhost names on webservers, and DNS subdomains using wordlists.

# Prerequisites
- [Python3](https://www.python.org/downloads/)
- [Requests](https://pypi.org/project/requests/)
- [Wordlists](https://github.com/danielmiessler/SecLists)

# Usage

```
usage: python3 URIDiscovery.py -m [MODE] -u [URL] -w [path/to/wordlist]

options:
  -h, --help            show this help message and exit
  -m MODE, --mode MODE  dir    Directory/file bruteforce mode
                        DNS    subdomain bruteforce mode
                        VHOST  bruteforce mode
  -u URL, --url URL     Address of Website
  -w WORDLIST, --wordlist WORDLIST
                        Path to wordlist
```


