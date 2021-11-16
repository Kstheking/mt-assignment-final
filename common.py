import csv
import json
import os
import pandas as pd
from tqdm.std import tqdm


base_url = 'https://japanesedictionary.org'
letter_list = ({'letter': 'a', 'page_count': 38}, {'letter': 'b', 'page_count': 25}, {'letter': 'c', 'page_count': 46}, {'letter': 'd', 'page_count': 25}, {
    'letter': 'e', 'page_count': 19}, {'letter': 'f', 'page_count': 21}, {'letter': 'g', 'page_count': 15}, {'letter': 'h', 'page_count': 17}, {'letter': 'i', 'page_count': 22}, {'letter': 'j', 'page_count': 4}, {'letter': 'k', 'page_count': 3}, {'letter': 'l', 'page_count': 14}, {'letter': 'm', 'page_count': 23}, {'letter': 'n', 'page_count': 9}, {'letter': 'o', 'page_count': 10}, {'letter': 'p', 'page_count': 38}, {'letter': 'q', 'page_count': 3}, {'letter': 'r', 'page_count': 21}, {'letter': 's', 'page_count': 51}, {'letter': 't', 'page_count': 24}, {'letter': 'u', 'page_count': 5}, {'letter': 'v', 'page_count': 8}, {'letter': 'w', 'page_count': 12}, {'letter': 'x', 'page_count': 1}, {'letter': 'y', 'page_count': 2}, {'letter': 'z', 'page_count': 1})
link_folder_path = 'links'
meanings_folder_path = "meanings"

def csv_to_excel(csv_file_path, excel_file_path):
    df = pd.read_csv(csv_file_path, sep="|")
    df = df.sort_values(by=['english'], ascending=True)
    df.to_excel(excel_file_path, index=False)


def get_subfolders(path):
    list_subfolders_path = [
        {'path': f.path, "name": f.name} for f in os.scandir(path) if f.is_dir()]
    return list_subfolders_path


def get_subfiles(path):
    list_subfiles_path = [
        {'path': f.path, 'name': f.name.split('.')[0]} for f in os.scandir(path) if f.is_file()]
    return list_subfiles_path


def json_to_csv_generator(json_file_path, csv_file_path):
    with open(json_file_path, 'r', encoding='utf8') as file_json:
        word_objects = json.load(file_json)
        with open(csv_file_path, 'w', encoding='utf8') as file_csv:
            field_names = ['english', 'type', 'japanese', 'hirangana', 'pronunciation', 'example_eng', 'example_jap']
            writer = csv.DictWriter(file_csv, delimiter='|', fieldnames=field_names)
            writer.writeheader()
            for word, word_definitions in tqdm(word_objects.items()):
                [writer.writerow({'english': word.replace(' ', '-').lower()+'_'+str(i+1), 'type': wd['type'], 'japanese': wd['japanese'], 'hirangana': wd['hirangana'],
                                  'pronunciation': wd['pronunciation'],  'example_eng': wd['example_eng'], 'example_jap': wd['example_jap']}) for i, wd in enumerate(word_definitions)]

def get_english_word_hindi_concept(h_concept_file_path):
    with open(h_concept_file_path,'r') as file:
        for line in file:
            print(line.rstrip()) 


print(get_english_word_hindi_concept("H_concept-to-mrs-rels.dat"))