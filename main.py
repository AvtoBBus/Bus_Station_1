import os
import requests
from bs4 import BeautifulSoup

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

num_page = 1
i = 0

while True:
    while i < 500:
        num_page += 1
        url = f"https://yandex.ru/images/search?p={num_page}&text=zebra&uinfo=sw-1536-sh-864-ww-760-wh-754-pd-1.25-wp-16x9_1920x1080&lr=51&rpt=image"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        list_of_src = []
        for link in soup.find_all("img"):
            print(link)
            list_of_src.append(link.get("src"))
        for list in list_of_src:
            if list.find("n=13") != -1:
                try:
                    list = "https:" + list
                    #print(list)
                    img = requests.get(list)
                    img_option = open(str(i) + ".jpg", "wb")
                    img_option.write(img.content)
                    img_option.close()
                    print("wow", i)
                except:
                    print("puk", i)
        i += 1