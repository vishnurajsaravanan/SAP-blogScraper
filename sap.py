from bs4 import BeautifulSoup
import requests
from stream import *
# import pandas as pd
# url = "https://blogs.sap.com/"

def get_url(dat_):
    response = requests.get(dat_)
    return response
web_link = get_url(dat_)

# data
def data(element = []):
    soup = BeautifulSoup(web_link.content, "html.parser" )
    elements = soup.find_all('ul')[0]
    # author_name = elements.find('div', class_="dm-user__heading").a.text
    # print(author_name)
    # author_content= soup.find('div', class_="dm-content-list-item__text dm-content-list-item__text--ellipsis")
    # print(author_content.text)
    # read_more = soup.find('div', class_="dm-content-list-item__text dm-content-list-item__text--ellipsis").a['href']
    # print(read_more)
    for i in range(len(elements)):
        auth_name = soup.find_all('a', class_='dm-user__name')[i]
        heading = soup.find_all('div', class_= "dm-contentListItem__title")[i].a
        auth_content = soup.find_all('div', class_="dm-content-list-item__text dm-content-list-item__text--ellipsis")[i]
        link = soup.find_all('div',class_="dm-content-list-item__text dm-content-list-item__text--ellipsis")[i].a['href']
        data = {"Author name" : auth_name.text,"Heading": heading.text,"Content" : auth_content.text, "Link" : link}
        # print(data, end="\n")
        element.append(data)
    return element




