import requests 
from bs4 import BeautifulSoup
page = requests.get("https://www.drugs.com/drug-interactions/ethinyl-estradiol-norgestimate,previfem.html")
soup = BeautifulSoup(page.content, 'html.parser')



div1 = soup.select("ul.interactions.ddc-list-unstyled li.int_1 a")
soup = BeautifulSoup(str(div1)[1:-1],'html.parser')
soup = BeautifulSoup(str(soup.extract()),'html.parser')
print(soup.extract())
for a in soup.find_all('a'):
    del a['href']
print(soup.contents)
for a in soup.find_all('a'):
    a.replaceWithChildren()
print(soup.contents)

soup = BeautifulSoup(page.content, 'html.parser')
div2 = soup.select("ul.interactions.ddc-list-unstyled li.int_2 a")
soup = BeautifulSoup(str(div2)[1:-1],'html.parser')
soup = BeautifulSoup(str(soup.extract()),'html.parser')
print(soup.extract())
for a in soup.find_all('a'):
    del a['href']
print(soup.contents)
for a in soup.find_all('a'):
    a.replaceWithChildren()
print(soup.contents)

soup = BeautifulSoup(page.content, 'html.parser')
div3 = soup.select("ul.interactions.ddc-list-unstyled li.int_3 a")
soup = BeautifulSoup(str(div3)[1:-1],'html.parser')
soup = BeautifulSoup(str(soup.extract()),'html.parser')
print(soup.extract())
for a in soup.find_all('a'):
    del a['href']
print(soup.contents)
for a in soup.find_all('a'):
    a.replaceWithChildren()
print(soup.contents) 