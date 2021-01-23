import requests 
from bs4 import BeautifulSoup
import re

class Overview:
    def __init__(self, link, name):
        self.__link = link
        self.__name = name
    def buildOverview(self):
        page = requests.get(self.__link)
        soup = BeautifulSoup(page.content, 'html.parser')
        description = soup.find_all("p")[2]
        f = open(self.__name+".txt", "w")
        f.write((self.__name).capitalize()+"\n")
        curr =re.sub('<a[^>]+>', '',str(description))
        f.write(curr.replace("<p>","").replace("</p>","").replace("</a>","")+"\n")
        f.close()