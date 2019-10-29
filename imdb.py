import requests
page = requests.get("https://www.imdb.com/?ref_=nv_home")

page.content

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')


soup.prettify()

import pandas as pd


import title.
pd.read_csv()

