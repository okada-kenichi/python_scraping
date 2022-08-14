import requests
from bs4 import BeautifulSoup

# UserAgentを偽装
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
header = {
    'User-Agent': user_agent
}
url = "https://okdd.jp/webapi/ipAddrChk.php"
response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "html.parser")
today = soup.find("body").text
print(today)