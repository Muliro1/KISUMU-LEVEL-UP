import requests
import requests
from requests.auth import HTTPBasicAuth

def access_token():
    consumer_key = "rgGpQ7legJvxpU2gSfEdkQfoeTuLmo3d"
    consumer_secret = "EpV0ojmRgMmVXJ3u"
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    return r.text





access_token = access_token()
api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
headers = { "Authorization": "Bearer %s" % access_token }
request = {
  "BusinessShortCode": "174379",
      "Password": "MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTgwNzAyMTQyOTAw",
      "Timestamp": "20180702142900",
      "TransactionType": "CustomerPayBillOnline",
      "Amount": "1",
      "PartyA": "2547",
      "PartyB": "174379",
      "PhoneNumber": "254727563415",
      "CallBackURL": "http://requestbin.fullcontact.com/1bz5y6t1",
      "AccountReference": "Muliro1",
      "TransactionDesc": "Muliro1"
}

response = requests.post(api_url, json = request, headers=headers)

print (response.text)