import requests 
from bs4 import BeautifulSoup
page = requests.get("https://www.drugs.com/mtm/previfem.html")
soup = BeautifulSoup(page.content, 'html.parser')


print(soup.find_all("p")[2])
