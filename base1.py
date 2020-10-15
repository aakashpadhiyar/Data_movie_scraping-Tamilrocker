from bs4 import BeautifulSoup as bs
import requests
from time import sleep
import re

# movies_list_url = "https://www.tamilrockermovies.vip/movies/page/0/"

movie_links_list = []

for i in range(20):
    sleep(1)
    movies_list_url = (f"https://www.tamilrockermovies.vip/movies/page/{i}/")
    req_site = requests.get(movies_list_url)
    beautify = bs(req_site.text, 'html.parser')
 
    link_list = beautify.find_all("article")
    for j in link_list:
        movie_single_link = j.find('a').get('href')
        #add link to list 
        movie_links_list.append(movie_single_link)

with open('MovieList.txt', 'w') as f:
    for item in movie_links_list:
        f.write("%s\n" % item)