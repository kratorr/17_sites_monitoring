# Sites Monitoring Utility

This program prints to the console status of sites.

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

pip install -r requirements.txt # alternatively try pip3

Remember, it is recommended to use virtualenv/venv for better isolation.

# Quickstart

The program must be run using the console, the required argument is the file with urls.

How to run:
```bash
$ python3 check_sites_health.py <file_path>
```
Example of script launch on Linux, Python 3.5:
```bash
$ python3 check_sites_health.py sites.txt 
URL: https://yandex.ru/
[OK] Server is avaliavle
[OK] Expiration date is more than a month

URL: https://pikabu.ru/
[OK] Server is avaliavle
[OK] Expiration date is more than a month

URL: https://www.google.ru/
[OK] Server is avaliavle
[OK] Expiration date is more than a month

URL: http://www.kratorr.com/
[X] Server is not avaliable
[OK] Expiration date is more than a month
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
