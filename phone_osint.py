#!/usr/bin/env python3
import sys
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import requests
import webbrowser

# ==== API Config ====
NUMVERIFY_API_KEY = "YOUR_NUMVERIFY_API_KEY"  # Add your key from numverify.com
NUMVERIFY_URL = "https://apilayer.net/api/validate"
IP_API_URL = "http://ip-api.com/json/"

def phone_lookup(phone):
    try:
        num = phonenumbers.parse(phone, None)
        print("\n=== Phone Info ===")
        print(f"Country      : {phonenumbers.region_code_for_number(num)}")
        print(f"Valid        : {phonenumbers.is_valid_number(num)}")
        print(f"Possible     : {phonenumbers.is_possible_number(num)}")
        print(f"Carrier      : {carrier.name_for_number(num, 'en')}")
        print(f"Time Zones   : {timezone.time_zones_for_number(num)}")
        print(f"Geo (approx) : {geocoder.description_for_number(num, 'en')}")
    except Exception as e:
        print(f"Error parsing phone number: {e}")

def numverify_lookup(phone):
    if NUMVERIFY_API_KEY == "YOUR_NUMVERIFY_API_KEY":
        print("\n[!] NumVerify API key not set. Skipping lookup.")
        return
    print("\n=== NumVerify Lookup ===")
    params = {"access_key": NUMVERIFY_API_KEY, "number": phone}
    try:
        r = requests.get(NUMVERIFY_URL, params=params)
        data = r.json()
        if data.get("valid"):
            print(f"Location : {data.get('location')} ({data.get('country_name')})")
            print(f"Carrier  : {data.get('carrier')}")
        else:
            print("NumVerify lookup failed or invalid key.")
    except Exception as e:
        print(f"NumVerify API error: {e}")

def social_media_search(phone):
    print("\n=== Social Media Search ===")
    sites = ["facebook.com", "linkedin.com", "instagram.com", "twitter.com"]
    for site in sites:
        url = f"https://www.google.com/search?q=\"{phone}\" site:{site}"
        print(f"[URL] {url}")
        # webbrowser.open(url)

def telegram_search(phone):
    print("\n=== Telegram Search ===")
    url = f"https://www.google.com/search?q=\"{phone}\" site:t.me OR site:telegram.me"
    print(f"[URL] {url}")
    # webbrowser.open(url)

def breach_lookup(phone):
    print("\n=== Breach DB Lookup ===")
    print(f"[URL] https://scylla.sh/search?q={phone}")
    print(f"[URL] https://dehashed.com/search?query={phone}")

def email_username_search(email):
    print("\n=== Email / Username OSINT ===")
    sites = ["facebook.com", "linkedin.com", "instagram.com", "github.com", "twitter.com"]
    for site in sites:
        url = f"https://www.google.com/search?q=\"{email}\" site:{site}"
        print(f"[URL] {url}")
        # webbrowser.open(url)

def ip_lookup(ip):
    print("\n=== IP Lookup ===")
    try:
        r = requests.get(f"{IP_API_URL}{ip}")
        data = r.json()
        if data.get("status") == "success":
            print(f"IP        : {ip}")
            print(f"ISP       : {data.get('isp')}")
            print(f"City      : {data.get('city')}, {data.get('regionName')}, {data.get('country')}")
            print(f"Lat / Lon : {data.get('lat')}, {data.get('lon')}")
        else:
            print("IP lookup failed.")
    except Exception as e:
        print(f"Could not fetch IP details: {e}")

def main():
    if len(sys.argv) < 2:
        phone = input("Enter phone number with country code (e.g. +919876543210): ").strip()
    else:
        phone = sys.argv[1]

    phone_lookup(phone)
    numverify_lookup(phone)
    social_media_search(phone)
    telegram_search(phone)
    breach_lookup(phone)

    email = input("\nEnter email from breach (if found) for deeper OSINT: ").strip()
    if email:
        email_username_search(email)

    if len(sys.argv) == 3:
        ip = sys.argv[2]
        ip_lookup(ip)
    else:
        ip_input = input("Enter IP address (optional): ").strip()
        if ip_input:
            ip_lookup(ip_input)

if __name__ == "__main__":
    main()
