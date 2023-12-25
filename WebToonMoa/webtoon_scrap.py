import requests
from bs4 import BeautifulSoup

url = "https://webtoon.kakao.com/original-webtoon?tab=mon"
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    webtoon_list = soup.select("div.flex.flex-wrap.gap-4.content-start > div")
    print(len(webtoon_list))
else : 
    print(response.status_code)