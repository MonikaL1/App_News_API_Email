import requests

api_key = "a8715c41714640fda4107c82e621bba4"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-02-21&sortBy=publishedAt&apiKey=a8715c41714640fda4107c82e621bba4"

#Make a request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

#Acces the article titles and decription
for article in content["articles"]:
    print(article["title"])
    print(article["description"])