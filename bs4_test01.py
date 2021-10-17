import requests
from bs4 import BeautifulSoup

url = "https://ja.wikipedia.org"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
today = soup.find("div", attrs={"id":"on_this_day"}).text
print(today)