import requests
url = "http://api.etherscan.io/api?module=stats&action=tokensupply&contractaddress=0xc58c0fca06908e66540102356f2e91edcaeb8d81&apikey=YourApiKeyToken"
response = requests.get(url)

supply=response.json()
currentsupply=int(supply.get("result"))
roundedsupply= int(currentsupply/int(1000000000000000000))

burnedtokens= int(1000000)-roundedsupply

print("remaining tokens =" ,roundedsupply)
print("total burned tokens =" ,burnedtokens)
print("initial supply = 1000000")