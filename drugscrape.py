import requests 
from bs4 import BeautifulSoup
page = requests.get("https://www.drugs.com/comments/ethinyl-estradiol-norgestimate/previfem.html")
print(page.status_code)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.find_all('p', class_="ddc-comment-content"))  #first like x reviews
print(soup.select("td.rating-score")) #scores for categories
print(soup.find_all(scope="row")) #categories
overall_score = soup.find_all(colspan="2")[-2] #overall score
print(overall_score)


