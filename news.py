import requests
import json
from datetime import datetime

date = datetime.today().strftime('%Y-%m-%d')
month = datetime.today().strftime('%Y-%m')

url = ('https://newsapi.org/v2/top-headlines?'
       'language=en&'
       'apiKey=yourapihere')
response = requests.get(url)

data = json.loads(response.text)

f = open("news-" + month + ".txt", "a")
f.write(date + "\n\n")

for x in range(10):
    sourcename = data["articles"][x]["source"]["name"]
    url = data["articles"][x]["url"]
    title = data["articles"][x]["title"]
    description = data["articles"][x]["description"]
    content = data["articles"][x]["content"]
    image = data["articles"][x]["urlToImage"]
    print(title)

    f.write("Source - " + sourcename + " ")
    f.write(url + "\n\n")
    f.write(title + "\n\n")
    f.write(description + "\n\n")
    f.write(content + "\n\n")
    if(x != 9):
        f.write("-------------------------------\n\n")
f.write("─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─|─\n\n")
f.close()
