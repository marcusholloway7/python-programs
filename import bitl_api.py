import bitl_api
API_USER="username"
API_KEY="Api_key"
bitly=bitly_api.Connection(API_USER, API_KEY)
response=bitly.shorten('www.example.com')
print(response)
