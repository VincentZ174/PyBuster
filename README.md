# PyBuster

Recreation of the (https://github.com/OJ/gobuster)[GoBuster] tool written in Python3. Bruteforce tool used to discover Web URIs for websites, Vhost names on webservers, and DNS subdomains.

# Getting Started

## Prerequisites
- [Python3](https://www.python.org/downloads/)
- [pynput](https://pypi.org/project/pynput/)

Note that these prerequisites will need to be installed on the victim machine. You can tackle this issue by creating an executable using a variety of tools. For more information refer to the "Creating an executable" section.


Run the script with this command:
```bash
python3 keylogger.py
```
Running the script backgrounded:
```bash
python keylogger.py &
```

# Creating an executable

You can tackle the issue of having to install python and pynput by "freezing" the python script. There are a number of tools that allow you to do so which can be viewed here: https://docs.python-guide.org/shipping/freezing/

