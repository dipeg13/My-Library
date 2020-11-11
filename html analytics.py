#Under construction
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

class Site():
    """a site"""
    
    def __init__(self, url):
        self.url = "https://"+url
        self.list_of_all_tags = ['h1','h2','h3','h4','h5','h6','section','article','header','footer','nav','aside','address','hgroup','base','html','head','title','style','meta','link','body','title','div','a','script','img','p','span','li','ul','br','input','form','strong','table','tbody','tr','td','dd','hr','figure','dt','dl','ol','pre','figcaption','main','content','template','element','shadow']
        self.raw_html = requests.get(self.url).content
        self.soup = BeautifulSoup(self.raw_html, 'html.parser')
        self.sites_tags = {}
    
    def basic_tags_counter(self):
        for index in self.list_of_all_tags:
            if len(self.soup(index))!= 0:
                self.sites_tags[index] = len(self.soup(index))
        print(self.sites_tags)
        tags_to_list = [(x, y) for x, y in self.sites_tags.items()]
        tags = [tags_to_list[i][0] for i in range(len(tags_to_list))]
        num = [tags_to_list[i][1] for i in range(len(tags_to_list))]
        fig1, ax1 = plt.subplots()
        ax1.pie(num, explode=None, labels=tags, autopct='%1.1f%%',
            shadow=True, startangle=90)
        ax1.axis('equal')
        plt.show()
        
if __name__ == "__main__":
    site = Site(input("Give a site's url (www.exaple.com): "))
    site.basic_tags_counter()
