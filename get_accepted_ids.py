import sys
import json
import requests
import environ

# reading .env file
env = environ.Env()
environ.Env.read_env()

url = 'https://lon.netverify.com/api/netverify/v2/acceptedIdTypes'
api_key = env('API_KEY')
api_secret = env('API_SECRET')
headers = {'user-agent': 'skybet test/0.1', 'content-type': 'application/json'}

def main():
    r = requests.get(url, auth=(api_key, api_secret), headers=headers)

    if r.headers['Content-Type'].startswith('application/json'):
        print(json.dumps(r.json()))
    else:
        print(r.text)

if __name__ == "__main__":
    main()
