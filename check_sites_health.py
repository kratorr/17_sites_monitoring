import requests
import whois
import datetime
import sys


def load_urls4check(path):
    with open(path, "r", encoding="utf-8") as urls_file:
        urls_list = urls_file.read().splitlines()
    return urls_list


def is_server_respond_with_200(url):
    try:
        response = requests.get(url)
        if response.ok:
            return True
    except requests.ConnectionError:
        return False


def get_domain_expiration_date(domain_name, days=30):
    whois_info = whois.whois(domain_name)
    expiration_date = whois_info.expiration_date
    delta_between_2_dates = expiration_date - datetime.datetime.now()
    days_delta = delta_between_2_dates.days
    if days_delta > days:
        return True
    else:
        return False

def print_site_status(url, server_availability, expiration_date):
    print("URL:", url)
    if server_availability:
        print("[OK] Server is avaliavle")
    else:
        print("[X] Server is not avaliable")
    if expiration_date:
        print("[OK] Expiration date is more than a month")
    else:
        print("[X] Expiration date is less than a month")
    print()


if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
        urls_list = load_urls4check(file_path)
    except IndexError:
        print("Arguments error")
        sys.exit()
    except FileNotFoundError:
        print("File not found")
        sys.exit()
    for url in urls_list:
        server_availability = is_server_respond_with_200(url)
        expiration_date = get_domain_expiration_date(url)
        print_site_status(url, server_availability, expiration_date)