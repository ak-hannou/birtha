import requests 
from bs4 import BeautifulSoup
import codecs
import re
class Reviews:
    def __init__(self,link,name):
        self.__link = link
        self.__name = name
    def buildReviews(self):
        #f = open(self.__name+".txt", "a")
        c = codecs.open(self.__name+".txt","a", encoding="utf-8")
        page = requests.get(self.__link)
        soup = BeautifulSoup(page.content, 'html.parser')
        reviews = (soup.find_all('p', class_="ddc-comment-content"))
        for review in reviews:
            c.write(str(review).replace("<p class=\"ddc-comment-content\">","").replace("</p>","").replace("</b>","").replace("<b>","").replace("			"," ")+"\n")
        scores = (soup.select("td.rating-score")) #scores for categories
        for score in scores:
            c.write(str(score).replace("<td class=\"rating-score\">","").replace("</td>","")+"\n")
        categories = (soup.find_all(scope="row")) #categories
        for cat in categories:
            curr = str(cat)
            curr =re.sub('<span[^>]+>', '',str(cat))
            c.write(curr.replace("</span>","").replace("</th>","").replace("<th>","").replace("<th scope=\"row\">","").replace("Off-label","")+"\n")
        if(len(soup.find_all(colspan="2")) != 1):
                print(len(soup.find_all(colspan="2")))
                overall_score = soup.find_all(colspan="2")[-2] #overall score
                c.write(str(overall_score).replace("<td colspan=\"2\">","").replace("</td>","")+"\n")
            
        c.close()


