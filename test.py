import requests
import json 
from bs4 import BeautifulSoup

# url_page = 'https://japanesedictionary.org/browse/letter/a/page-2'
# session = requests.Session()
# page = session.get(url_page)
# soup = BeautifulSoup(page.content, 'html.parser')
# entries = soup.find_all('td', {'class': 'english'})
# raw_links = [e.find('a') for e in entries]
# word_links = [(l.text, l['href']) for l in raw_links]
# print(word_links)

url_page = 'https://japanesedictionary.org/translate-english/about'
session = requests.Session()
page = session.get(url_page)
soup = BeautifulSoup(page.content, 'html.parser')

word_english = soup.find('td', {'class': 't_english t_data'}).text
word_types = [w_type.text for w_type in soup.find_all('td', {'class': 't_type t_data'})]
word_japaneses = [w_jap.text for w_jap in soup.find_all('td', {'class': 't_japanese t_data'})]
word_hiraganas = [w_hir.text for w_hir in soup.find_all('td', {'class': 't_hiragana t_data'})]
word_pronunciations = [w_pro.text for w_pro in soup.find_all('td', {'class': 't_pronunciation t_data'})]
word_examples = [(w_ex.find('dt').text, w_ex.find('dd').text) for w_ex in soup.find_all('td', {'class': 't_sentence t_data'})]
word_array = [{'type':wt, 'japanese':wh, 'hirangana':wh, 'pronunciation':wp, 'example_eng':we[0], 'example_jap':we[1]} for wt, wj, wh, wp, we in zip(word_types, word_japaneses, word_hiraganas, word_pronunciations, word_examples)]
word_object = {word_english : word_array}

with open("sample.json", "w") as outfile:
    json.dump(word_object, outfile)