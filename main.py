import requests
import send_email

# Our personal API
api_key = "0fc34c3d866047af97b8ce3de77d7391"

# The url that we are going to get data
url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=0fc34c3d866047af97b8ce3de77d7391"

request = requests.get(url)

# We are extracting the url variable into this
# .json() method is used to convert that variable into a dictionary rather than a string
content = request.json()

# We've set-up a body variable to contain the strings. I set-up as an empty for now because we are going to fill that thing later in the for-loop
body = ""
for article in content["articles"]:
    body = body + article["title"] + "\n" + article["description"] + 2*"\n"

# This is added to ensure that there are other values in the key that have unicode characters which python could not handle
body = body.encode('utf-8')

# We've sent the variable into the actual sending of the email in different file
send_email.send_email(body)
