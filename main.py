import requests
from send_email import send_email

api_key = "a8715c41714640fda4107c82e621bba4"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-02-21&sortBy=publishedAt&apiKey=a8715c41714640fda4107c82e621bba4"

#Make a request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

#Acces the article titles and decription
body = " "
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)