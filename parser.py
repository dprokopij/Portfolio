import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'}


def array():
    for count in range(1, 21):

        sleep(3)

        url = f"https://kaspi.kz/shop/c/snowboards/?page={count}"


        response = requests.get(url, headers=headers)

        soup = BeautifulSoup(response.text, "lxml")

        data = soup.find_all("div", class_="item-card ddl_product")

        for i in data:

            name = i.find("a", class_="item-card__name").text
            price = i.find("span", class_="item-card__prices-price").text
            url_product = "https://kaspi.kz" + i.find("a", class_="item-card__image-wrapper").get("href")

            yield name, price, url_product
