import json
import os
import shutil

import os
import shutil
import requests
import multiprocessing as mp
from tqdm import tqdm
from bs4 import BeautifulSoup
from common import link_folder_path, get_subfolders, base_url, get_subfiles


meanings_folder_path = "meanings"


def write_to_json(object, file_path):
    with open(file_path+".json", "w+", encoding='utf-8') as outfile:
        json.dump(object, outfile, indent=4, ensure_ascii=False)


def get_words_url(file):
    with open(file['path']) as file:
        lines = [line.strip() for line in file.readlines()]
        return lines


def fetch_meaning_from_url(url, session):
    page = session.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    word_english = soup.find('td', {'class': 't_english t_data'}).text
    word_types = [w_type.text for w_type in soup.find_all(
        'td', {'class': 't_type t_data'})]
    word_japaneses = [w_jap.text for w_jap in soup.find_all(
        'td', {'class': 't_japanese t_data'})]
    word_hiraganas = [w_hir.text for w_hir in soup.find_all(
        'td', {'class': 't_hiragana t_data'})]
    word_pronunciations = [w_pro.text for w_pro in soup.find_all(
        'td', {'class': 't_pronunciation t_data'})]
    word_examples = [(w_ex.find('dt').text, w_ex.find('dd').text)
                     for w_ex in soup.find_all('td', {'class': 't_sentence t_data'})]
    word_array = [{'type': wt, 'japanese': wj, 'hirangana': wh, 'pronunciation': wp, 'example_eng': we[0], 'example_jap':we[1]}
                  for wt, wj, wh, wp, we in zip(word_types, word_japaneses, word_hiraganas, word_pronunciations, word_examples)]
    word_object = {word_english: word_array}
    return word_object


def worker(words_folder):
    session = requests.Session()
    words_folder_path = words_folder["path"]
    words_folder_name = words_folder["name"]
    files = get_subfiles(words_folder_path)

    parent_folder = meanings_folder_path+"/" + words_folder_name
    os.mkdir(parent_folder)
    for file in tqdm(files):
        words_url = get_words_url(file)
        meanings = {}
        for url in words_url:
            meaning = fetch_meaning_from_url(base_url+url, session)
            meanings.update(meaning)
        # print(meanings)
        write_to_json(meanings, parent_folder+"/"+file['name'])


def meaning_fetch():
    path = meanings_folder_path
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        shutil.rmtree(path)
        os.makedirs(path)
    p = mp.Pool(26)
    words_folders = get_subfolders(link_folder_path)
    p.map(worker, words_folders)
    p.close()
    p.join()




meaning_fetch()
