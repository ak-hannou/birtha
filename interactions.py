import requests 
from bs4 import BeautifulSoup
page = requests.get("https://www.drugs.com/drug-interactions/ethinyl-estradiol-norgestimate,previfem.html")
soup = BeautifulSoup(page.content, 'html.parser')



div1 = soup.select("ul.interactions.ddc-list-unstyled li.int_1 a")

print(div1)

div2 = soup.select("ul.interactions.ddc-list-unstyled li.int_2 a")

print(div2)

div3 = soup.select("ul.interactions.ddc-list-unstyled li.int_3 a")

print(div3)