import requests
import json 

url = "https://iata-and-icao-codes.p.rapidapi.com/airlines"

headers = {
    'x-rapidapi-host': "iata-and-icao-codes.p.rapidapi.com",
    'x-rapidapi-key': "8a0ee99658msh391f0be5aa5d17fp170073jsnc2213f30ccc8"
    }

response = requests.request("GET", url, headers=headers)

jsonobj = json.loads(response.text)

i = 0
result = "<TABLE border='1'>"
for key in jsonobj:
   result += '<TR>'
   print(key)
   for k,v in key.items():
       result += "<TD>{}</TD><TD>{}</TD>".format(k,v)
   result += "</TR>"
   break;

result += "</TABLE>"
print(result)

