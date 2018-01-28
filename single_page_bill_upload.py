import sys
import json
import io
import requests
import environ

# reading .env file
env = environ.Env()
environ.Env.read_env()

url = 'https://acquisition.lon.netverify.com/api/netverify/v2/acquisitions/complete'
api_key = env('API_KEY')
api_secret = env('API_SECRET')

headers = {
    'accept': 'application/json',
    'user-agent': 'skybet test/0.1'
}

metadata = {
    "type": "UB",
    "country": "GBR",
    "merchantScanReference": "myScanReference",
    "customerId": "MyCustomerId"
}

def upload(filepath):
    file_suffix = filepath[-3:]
    if file_suffix == 'pdf':
        mime_type = 'application/pdf'
    elif file_suffix == 'png':
        mime_type = 'image/png'
    elif file_suffix == 'jpg':
        mime_type = 'image/jpg'
    else:
        print("invalid doc type")
        exit(0)

    filename = 'image.{}'.format(file_suffix)           
    files = [
        ('image', (filename, open(filepath, 'rb'), mime_type)),
        ('metadata', json.dumps(metadata))
    ]

    r = requests.post(
        url,
        auth=(api_key, api_secret),
        headers=headers,
        files=files
    )

    if r.headers['Content-Type'].startswith('application/json'):
        print(r.json())
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
