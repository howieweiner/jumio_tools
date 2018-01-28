# Intro
This repo contains a set of Python scripts to interact with the [Jumio Verification API](https://github.com/Jumio/implementation-guides)

## Install Python environment
Firstly, ensure you have python 3 installed

`brew install python3`

Now create virtual environment (so we don;t pollute global python packages with those used for this project). This is a one-off task. It will create a folder in the project named `venv` to hold all libraries.

`python3 -m venv venv`

Now activate the virtual environment. This should be done every time you use the scripts in this project

`source venv/bin/activate`

Now install the required libraries - a one-off task

`pip install -r requirements.txt`

Creat a `.env` file to store your API credentials (copy over `sample.env`)

## Usage

### ID APIs
`python driving_licence_upload.py [path to file]`

`python get_accepted_ids.py`

`python get_id_scan_status.py [jumio scan id]`

`python get_id_scan_details.py [jumio scan id]`

`python get_id_scan_document_details.py [jumio scan id]`

`python get_id_scan_images.py [jumio scan id]`

### Bill APIs
`python single_page_bill_upload.py [path to file]`

`python multi_page_bill_upload.py [path to file]`

`python get_bill_scan_status.py [jumio scan id]`

`python get_bill_scan_details.py [jumio scan id]`

`python get_bill_scan_document_details.py [jumio scan id]`

`python get_bill_scan_images.py [jumio scan id]`

### Examining Responses
It is recommended to use [jq](https://stedolan.github.io/jq/) to examine responses e.g.

`python get_bill_scan_status.py [jumio scan id]` | jq ".status"`

### Notes
You can safely add any id documents to thr `docs` folder as this is ignored by Git




