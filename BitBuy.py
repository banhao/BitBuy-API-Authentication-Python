#!/usr/bin/env python3

# Author: banhao@gmail.com
# Version:
# Issue Date:
# Release Note:


import json, hmac, hashlib, time, requests, base64, collections
from requests.auth import AuthBase
import urllib.parse as urlparse
from urllib.parse import unquote, urlencode
from datetime import datetime, timedelta, date


api_key = ''
secret_key = ''


timestamp = str(int(time.time()))
api_url = 'https://partner.bcm.exchange/api/v1/coins'
url_parts = list(urlparse.urlparse(api_url))
url_params = {'apikey': api_key, 'stamp': timestamp}
query = dict(urlparse.parse_qsl(url_parts[4]))
query.update(url_params)
url_parts[4] = urlencode(query)
url = urlparse.urlunparse(url_parts)
print(url)

sigContent = {
    'path' : list(urlparse.urlparse(url))[2], 
    'query' : list(urlparse.urlparse(url))[4], 
    'content-length' : -1
    }
print(sigContent)
hmac_key = bytes(secret_key, 'utf-8')
signature = hmac.new(hmac_key, str(sigContent).encode('utf-8'), hashlib.sha256).hexdigest()
print(signature)
signature_b64 = base64.b64encode(bytes.fromhex(signature)).decode()
print(signature_b64)
headers = {
    'Content-Type' : 'application/json',
    'signature' : signature_b64
    }
print(headers)
body = {}
products = requests.request('GET', url, data = body, headers = headers)
print(products)
