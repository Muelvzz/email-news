import requests

# Our personal API
api_key = "0fc34c3d866047af97b8ce3de77d7391"

# The url that we are going to get data
url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=0fc34c3d866047af97b8ce3de77d7391"

request = requests.get(url)

# We are extracting the url variable into this
# .json() method is used to convert that variable into a dictionary rather than a string
content = request.json()

for article in content["articles"]:
    print(article["author"])
    print(article["title"])
    print(article["description"])
    print(article["content"])
    print(" ")
