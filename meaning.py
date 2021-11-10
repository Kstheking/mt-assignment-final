import os
import shutil

import os
import shutil
import requests
import multiprocessing as mp
from tqdm import tqdm
from bs4 import BeautifulSoup
from common import base_url, letter_list, get_subfiles


meanings_folder_path = "meanings"
letter_links_folder_path = (meanings_folder_path+'/{letter}')


def worker(words_folder):
    session = requests.Session()
    words_folder_path = words_folder["path"]
    words_folder_name = words_folder["name"]
    files = get_subfiles(words_folder_path)

    parent_folder = meanings_folder_path+"/" + words_folder_name
    os.mkdir(parent_folder)
    for file in tqdm(files):
        fetch_meanings(file, session)


def fetch_meanings(file, session):
    with open(file['name']) as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        


def meaning_fetch():
    path = meanings_folder_path
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        shutil.rmtree(path)
        os.makedirs(path)
    p = mp.Pool(26)
    words_folders = letter_links_folder_path
    p.map(worker, words_folders)
    p.close()
    p.join()
