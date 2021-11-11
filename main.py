import re
from urllib.request import urlopen
from bs4 import BeautifulSoup as bS

card_name_input = input("What MID card are you looking for?\n")
card_name = card_name_input.replace(" ", "-")

url = f"https://www.cardmarket.com/de/Magic/Products/Singles/Innistrad-Midnight-Hunt/{card_name}"
page = urlopen(url)
html = page.read().decode("utf-8")

soup = bS(html, "lxml")

price_tag = soup.find('dt', string="Preis-Trend").next_sibling.find('span')
price = price_tag.string

title = soup.title.string
title = title.replace(" | Cardmarket", "")

print(title)
print(f"Preis-Trend: {price}")
