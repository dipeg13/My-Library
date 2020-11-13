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
        final_list = []
        list_of_links = []
        soup = BeautifulSoup(req_con, "html.parser")
        results = []
        flag = "&sa="
        for links in soup.find_all('a', href=True):
            if "url" in links["href"] and (links["href"].strip("/url?q=")[:12] == "https://www." or links["href"].strip("/url?q=")[:11] == "http://www." or links["href"].strip("/url?q=")[:4] == "www."):
                list_of_links.append(links['href'].strip("/url?q="))
        for links in list_of_links:
            links = links[:links.index(flag)]
            final_list.append(links)
        print("Number of results: "+str(len(list_of_links)))
        return final_list

#sites returns the raw url of the sites found at search method 
def sites():
    sites_list = search()
    final_list = []
    for i in range(len(sites_list)):
        if "https://" in sites_list[i]:
            sites_list[i] = sites_list[i].split("https://")
        elif "http://" in sites_list[i]:
            sites_list[i] = sites_list[i].split("http://")
        final_list.append(sites_list[i][1][:sites_list[i][1].index("/")])
    for i in final_list:
        print(i)
    return final_list

#clean_sites returns a list with no doublicated sites and without google.com
def clean_sites():
    sites_list = sites()
    cleaned_list = list(dict.fromkeys(sites_list))
    print("Number of cleaned results: "+str(len(cleaned_list)))
    if "www.google.com" in cleaned_list:cleaned_list.remove("www.google.com")
    for i in cleaned_list:
        print(i)
    return cleaned_list
