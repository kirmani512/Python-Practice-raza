import requests
import json

query=input("get the news of?")
url=f"https://newsapi.org/v2/everything?q={query}&from=2025-06-25&sortBy=publishedAt&apiKey=7118fdd5b42f48b290db145f2e7e6184"
r=requests.get(url)
news=json.loads(r.text)
# print(news,type(news))

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("----------------------------------------------")