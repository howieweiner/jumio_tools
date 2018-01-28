import sys
import json
import requests
import environ

# reading .env file
env = environ.Env()
environ.Env.read_env()

url = 'https://retrieval.lon.netverify.com/api/netverify/v2/documents/{}/data/document'
api_key = env('API_KEY')
api_secret = env('API_SECRET')
headers = {'user-agent': 'skybet test/0.1', 'content-type': 'application/json'}

def get_details(scan_id):
    r = requests.get(
        url.format(scan_id),
        auth=(api_key, api_secret),
        headers=headers
        )

    if r.headers['Content-Type'].startswith('application/json'):
        print(json.dumps(r.json()))
    else:
        print(r.text)

def main():
    if len(sys.argv) < 2:
        print("Please provide a Jumio scan id")
        exit(0)
    scan_id = sys.argv[1]
    get_details(scan_id)

if __name__ == "__main__":
    main()
