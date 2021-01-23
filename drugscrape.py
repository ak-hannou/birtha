import requests 
from bs4 import BeautifulSoup
page = requests.get("https://www.drugs.com/comments/norethindrone/errin.html")
print(page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')
#printprint(soup.prettify())

print(soup.find_all('p', class_="ddc-comment-content"))
print(soup.select("td.rating-score"))
print(soup.find_all(scope="row"))

