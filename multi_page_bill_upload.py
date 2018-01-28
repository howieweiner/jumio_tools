import sys
import json
import requests
import environ

# reading .env file
env = environ.Env()
environ.Env.read_env()

api_key = env('API_KEY')
api_secret = env('API_SECRET')

initiate_url = 'https://acquisition.lon.netverify.com/api/netverify/v2/acquisitions'

initiate_headers = {
    'accept': 'application/json',
    'user-agent': 'skybet test/0.1',
    'content-type': 'application/json'
}
initiate_data = {
    "country": "GBR",    
    "type": "UB",
    "merchantScanReference": "myScanReference",
    "customerId": "MyCustomerId",
}

upload_url = 'https://acquisition.lon.netverify.com/api/netverify/v2/acquisitions/{}/document'

finalise_url ='https://acquisition.netverify.com/api/netverify/v2/acquisitions/{}'

upload_headers = {
    'accept': 'application/json',
    'user-agent': 'skybet test/0.1',
}

def initiate():
    r = requests.post(
        initiate_url,
        auth=(api_key, api_secret),
        headers=initiate_headers,
        data=json.dumps(initiate_data) # we are not form-encoding this POST request. We must JSON encode the data
        )

    json_response = r.json()
    scan_ref = json_response['scanReference']
    return scan_ref

def upload(scan_ref, filepath):
    files = [
        ('image', ('image.pdf', open(filepath, 'rb'), 'application/pdf')),
    ]
    r = requests.post(
        upload_url.format(scan_ref),
        auth=(api_key, api_secret),
        headers=upload_headers,
        files=files
    )

    if r.headers['Content-Type'].startswith('application/json'):
        print(json.dumps(r.json()))
    else:
        print(r.text)

def finalise(scan_ref):
    
def main():
    if len(sys.argv) < 2:
        print("Please provide a filepath to upload")
        exit(0)
    filepath = sys.argv[1]

    scan_ref = initiate()
    upload(scan_ref, filepath)
    finalise(scan_ref)


if __name__ == "__main__":
    main()
