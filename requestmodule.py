import requests
from bs4 import BeautifulSoup

# response=requests.get("https://computerzone.pk/")

# print(response.text)

url="https://computerzone.pk/"
r=requests.get(url)


soup=BeautifulSoup(r.text,'html.parser') #parse the html

# print(soup.prettify) # make a visually appealing data presentation

for heading in soup.find_all("p"):  #gives tha data in paragraph tag
    print(heading.text)