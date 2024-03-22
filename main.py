import requests
from send_email import send_email

topic = "tesla"
api_key = "a8715c41714640fda4107c82e621bba4"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2024-02-21&" \
      "sortBy=publishedAt&apiKey=a8715c41714640fda4107c82e621bba4&" \
      "language=en"

#Make a request
request = requests.get(url)

#Get a dictionary with data
content = request.json()

#Acces the article titles and decription
body = " "
for article in content["articles"][:20]:
    if article["title"] is  None:

            body = "Subject: Today's news"\
               + "\n" + body + article["title"] + "\n" \
               + article["description"] \
               + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)















