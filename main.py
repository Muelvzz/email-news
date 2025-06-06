import requests

# Our personal API
api_key = "0fc34c3d866047af97b8ce3de77d7391"

# The url that we are going to get data
url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=0fc34c3d866047af97b8ce3de77d7391"

# I don't know how this works but is supposed to prevent your terminal from sending too many request on Edge

request = requests.get(url)

# We are extracting the url variable into this
content = request.text

# This prints the url variable
print(content)
