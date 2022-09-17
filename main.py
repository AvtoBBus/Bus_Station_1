import requests
from bs4 import BeautifulSoup

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
}

def Search_zebra():
    num_page = 1
    i = 0
    while True:
        print("=" * 100)
        print("\nStart searching images with zebra\n")
        print("=" * 100)
        while i < 100:
            num_page += 1
            url = f"https://yandex.ru/images/search?p={num_page}&text=zebra&uinfo=sw-1536-sh-864-ww-760-wh-754-pd-1.25-wp-16x9_1920x1080&lr=51&rpt=image"
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')

            list_of_src = []
            for link in soup.find_all("img"):
                if link.find("captcha") != -1:
                    Search_Bay_Horse()
                print(link)
                list_of_src.append(link.get("src"))
            for list in list_of_src:
                if list.find("n=13") != -1:
                    try:
                        link = "https:" + list
                        img = requests.get(link)
                        img_option = open(str(i) + ".jpg", "wb")
                        img_option.write(img.content)
                        img_option.close()
                        i += 1
                        print("wow", i)
                    except:
                        print("puk", i)

def Search_Bay_Horse():
    num_page = 1
    i = 0
    while True:
        print("=" * 100)
        print("\nStart searching images with bay horse\n")
        print("=" * 100)
        while i < 100:
            num_page += 1
            url = f"https://yandex.ru/images/search?p={num_page}&from=tabbar&text=bay%20horse&lr=51&rpt=image&uinfo=sw-1920-sh-1080-ww-1220-wh-970-pd-1-wp-16x9_1920x1080"
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')

            list_of_src = []
            for link in soup.find_all("img"):
                if link.find("captcha") != -1:
                    Finish()
                print(link)
                list_of_src.append(link.get("src"))
            for list in list_of_src:
                if list.find("n=13") != -1:
                    if list.find("captcha") != -1:
                        Finish()
                    try:
                        link = "https:" + list
                        img = requests.get(link)
                        img_option = open(str(i) + ".jpg", "wb")
                        img_option.write(img.content)
                        img_option.close()
                        i += 1
                        print("wow", i)
                    except:
                        print("puk", i)

def Finish():
    print("\nProgram has finished!\n")
    exit(0)

def main():
    Search_zebra()

if __name__ == '__main__':
    main()