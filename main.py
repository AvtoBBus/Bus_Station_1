import os
import requests
from bs4 import BeautifulSoup

url = 'https://yandex.ru/images/search?text=zebra'
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

list_of_href = []
for link in soup.find_all("img"):
        list_of_href.append(link.get("src"))
i = 0
for list in list_of_href:
    if list.find("n=13") != -1:
        try:
            list = "https:" + list
            print(list)
            img = requests.get(list)
            img_option = open(str(i) + ".jpg", "wb")
            img_option.write(img.content)
            img_option.close()
            i += 1
            print("wow", i)
        except:
            print("puk", i)
