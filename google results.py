import requests
from bs4 import BeautifulSoup

#search() returns a list of links for the top results of a given topic

def search():
    search = input("Give a search title: ")
    print("Top Google's result links for topic >>{}<<".format(search))
    url = f"https://www.google.com/search?client=firefox-b-d&q={search}"
    req = requests.get(url)
    req_con = req.content

    if req.status_code !=200:
        print("connection error")
    else:
        list_of_links = []
        soup = BeautifulSoup(req_con, "html.parser")
        results = []
        flag = "&sa="
        for links in soup.find_all('a', href=True):
            if "url" in links["href"] and (links["href"].strip("/url?q=")[:12] == "https://www." or links["href"].strip("/url?q=")[:11] == "http://www." or links["href"].strip("/url?q=")[:4] == "www."):
                list_of_links.append(links['href'].strip("/url?q="))
        for links in list_of_links:
            links = links[:links.index(flag)]
            print(links)
        print("Number of results: "+str(len(list_of_links)))
        return list_of_links
    
search()
