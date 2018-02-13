import requests
import whois #python-whois
import datetime
import sys
import os


def load_urls4check(path):
    with open(path, "r", encoding="utf-8") as urls_file:
        urls_list = urls_file.read().splitlines()
    return urls_list


def is_server_respond_with_200(url):
    try:
        request = requests.get(url)
        if request.status_code == 200:
            return True
    except:
        return False


def get_domain_expiration_date(domain_name):
    whois_info = whois.whois(domain_name)
    expiration_date = whois_info.expiration_date
    return expiration_date


if __name__ == "__main__":
    try:
        file_path = sys.argv[1]
        if os.path.isfile(file_path):
            urls_list = load_urls4check(file_path)
            for url in urls_list:
                avaliable_server = is_server_respond_with_200(url)
                expiration_date = get_domain_expiration_date(url)
                now_date = datetime.datetime.now()
                delta_between_2_dates = expiration_date - now_date
                day_delta = delta_between_2_dates.days
                print("URL:", url)
                if avaliable_server:
                    print("[OK] Server is avaliavle")
                else:
                    print("[X] Server is not avaliable")
                if day_delta < 30:
                    print("[X] Expiration date is less than a month")
                elif day_delta > 30:
                    print("[OK] Expiration date is more than a month")
                print()
        else:
            print("File not found")
    except IndexError:
        print("Arguments error")