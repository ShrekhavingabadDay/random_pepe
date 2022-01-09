import requests
import re
from bs4 import BeautifulSoup

rare_pepes = "https://rare-pepe.com/"

r = requests.get(rare_pepes)

soup = BeautifulSoup(r.text, 'html.parser')

image_sources = [image['src'] for image in soup.findAll('img')]

with open('pepe_links.txt', 'w') as f:
    for image_src in image_sources:
        full_link = re.sub('-[0-9]+x[0-9]+','',image_src)
        f.write(full_link+'\n')
