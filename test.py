import requests
from bs4 import BeautifulSoup
    

url_page = 'https://japanesedictionary.org/browse/letter/a/page-2'
session = requests.Session()
page = session.get(url_page)
soup = BeautifulSoup(page.content, 'html.parser')
entries = soup.find_all('td', {'class': 'english'})
raw_links = [e.find('a') for e in entries]
word_links = [(l.text, l['href']) for l in raw_links]
print(word_links)