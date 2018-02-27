import requests
import whois
import datetime
import sys


def load_urls4check(path):
    with open(path, "r", encoding="utf-8") as urls_file:
        urls_list = urls_file.read().splitlines()
    return urls_list


def is_server_respond_with_ok(url):
    try:
        response = requests.get(url)
        return response.ok
    except requests.ConnectionError:
        return False


def check_domain_expiration_date(domain_name, days=30):
    whois_info = whois.whois(domain_name)
    expiration_date = whois_info.expiration_date
    if expiration_date is None:
        pass
    else:
        if type(expiration_date) == list:
            expiration_date = min(expiration_date)
        delta_between_2_dates = expiration_date - datetime.datetime.now()
        days_delta = delta_between_2_dates.days
        return days_delta > days


def print_site_status(url, server_availability, expiration_date):
    print("URL:", url)
    print("{} Server is avaliable".format(
            "[OK]" if server_availability else "[X]"))
    print("{} Expiration date is more than a month".format(
            "[OK]" if expiration_date else "[X]"))
    print()


if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
        urls_list = load_urls4check(file_path)
    except IndexError:
        sys.exit("Arguments error")
    except FileNotFoundError:
        sys.exit("File not found")
    for url in urls_list:
        server_availability = is_server_respond_with_ok(url)
        expiration_date = check_domain_expiration_date(url)
        print_site_status(url, server_availability, expiration_date)