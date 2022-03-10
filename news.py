import requests
import json
from datetime import datetime

newsPerDay = 10
path = "/home/name/YOUR_PATH"

date = datetime.today().strftime('%Y-%m-%d')
month = datetime.today().strftime('%Y-%m')

url = ('https://newsapi.org/v2/top-headlines?'
       'language=en&'
       'apiKey=YOUR_API_KEY_HERE')
response = requests.get(url)

data = json.loads(response.text)

f = open(path + "/news-" + month + ".txt", "a")
g = open(path + "/images-" + month + ".txt", "a")
f.write(date + "\n\n")

for x in range(newsPerDay):
    article = data["articles"][x]

    sourcename = article["source"]["name"]
    url = article["url"]
    title = article["title"]
    description = article["description"]
    content = article["content"]
    image = article["urlToImage"]

    if(sourcename == None):
        sourcename = "no source"

    if(url == None):
        url = "no url"

    if(title == None):
        title = "no title"

    if(description == None):
        description = "no description"

    if(content == None):
        content = "no content"

    f.write("Source - " + sourcename + " " + url + "\n\n" +
            title + "\n\n" + description + "\n\n" + content + "\n\n")

    g.write(image + "\n")

    if(x != newsPerDay - 1):
        f.write("-------------------------------\n\n")
f.write("─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─\n\n")
f.close()
g.close()
