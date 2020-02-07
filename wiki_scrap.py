from pkgutil import get_data

from bs4 import BeautifulSoup
import urllib.request
import os


def search_spider():
    url = "https://en.wikipedia.org/wiki/Deep_learning"
    source_code = urllib.request.urlopen(url)
    plain_text = source_code
    soup = BeautifulSoup(plain_text, "html.parser")
    print(soup.title.string)
    result_list = soup.findAll('a')
    print(result_list)
    for i in result_list:
        link = i.get('href')
        print(link)


search_spider()
