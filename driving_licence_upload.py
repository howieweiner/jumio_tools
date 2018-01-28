import sys
import json
import base64
import requests
import environ

# reading .env file
env = environ.Env()
environ.Env.read_env()

api_key = env('API_KEY')
api_secret = env('API_SECRET')

url = 'https://lon.netverify.com/api/netverify/v2/performNetverify'

headers = {
    'accept': 'application/json',
    'user-agent': 'skybet test/0.1',
    'content-type': 'application/json'
}

def upload(filepath):
    data = {
        "merchantIdScanReference": "myScanReference",
        "country": "GBR",    
        "idType": "DRIVING_LICENSE"
    }
    
    with open(filepath, "rb") as image_file:
        encoded_img = base64.b64encode(image_file.read())
        data["frontsideImage"] = "{}".format(encoded_img.decode('utf-8'))

    r = requests.post(
        url,
        auth=(api_key, api_secret),
        headers=headers,
        data=json.dumps(data)
    )

    if r.headers['Content-Type'].startswith('application/json'):
        print(json.dumps(r.json()))
    else:
        print(r.text)

def main():
    if len(sys.argv) < 2:
        print("Please provide a filepath to upload")
        exit(0)
    filepath = sys.argv[1]
    upload(filepath)


if __name__ == "__main__":
    main()
