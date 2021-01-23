import requests 
from bs4 import BeautifulSoup
import re
class Interactions:
    def __init__(self,link,name):
         self.__link = link
         self.__name = name
    def buildInteractions(self):
        f = open(self.__name+".txt", "a")   
        page = requests.get(self.__link)
        soup = BeautifulSoup(page.content, 'html.parser')
        div1 = (soup.select("ul.interactions.ddc-list-unstyled li.int_1 a")) 
        soup = BeautifulSoup(str(div1)[1:-1],'html.parser')
        soup = BeautifulSoup(str(soup.extract()),'html.parser')
        level1 = str(soup)
        if(level1.strip()==""):
            f.write("No level 1 interactions\n")
        else:
            f.write("Level 1 interactions:\n")
            for level in soup:
                curr =re.sub('<a href=[^>]+>', '',str(level))
                if(curr[0] != ','):
                    f.write(curr.replace('</a>',"")+"\n")
                
        
        soup = BeautifulSoup(page.content, 'html.parser')
        div2 = soup.select("ul.interactions.ddc-list-unstyled li.int_2 a")
        soup = BeautifulSoup(str(div2)[1:-1],'html.parser')
        soup = BeautifulSoup(str(soup.extract()),'html.parser')
        level2 = str(soup)
        if(level2.strip()==""):
            f.write("No level 2 interactions\n")
        else:
            f.write("Level 2 interactions:\n")
            for level in soup:
                curr =re.sub('<a href=[^>]+>', '',str(level))
                if(curr[0] != ','):
                    f.write(curr.replace('</a>',"")+"\n")

        soup = BeautifulSoup(page.content, 'html.parser')
        div3 = soup.select("ul.interactions.ddc-list-unstyled li.int_3 a")
        soup = BeautifulSoup(str(div3)[1:-1],'html.parser')
        soup = BeautifulSoup(str(soup.extract()),'html.parser')
        level3 = str(soup)
        if(level3.strip()==""):
            f.write("No level 3 interactions\n")
        else:
            f.write("Level 3 interactions:\n")
            for level in soup:
                curr =re.sub('<a href=[^>]+>', '',str(level))
                if(curr[0] != ','):
                    f.write(curr.replace('</a>',"")+"\n")
        f.close()