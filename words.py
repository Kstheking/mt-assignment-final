import multiprocessing as mp
import os
import shutil

arguments = ({'letter': 'a', 'last_page': 38}, {'letter': 'b', 'last_page': 25}, {'letter': 'c', 'last_page': 46}, {'letter': 'd', 'last_page': 25}, {
             'letter': 'e', 'last_page': 19}, {'letter': 'f', 'last_page': 21}, {'letter': 'g', 'last_page': 15}, {'letter': 'h', 'last_page': 17}, {'letter': 'i', 'last_page': 22}, {'letter': 'j', 'last_page': 4}, {'letter': 'k', 'last_page': 3}, {'letter': 'l', 'last_page': 14}, {'letter': 'm', 'last_page': 23}, {'letter': 'n', 'last_page': 9}, {'letter': 'o', 'last_page': 10}, {'letter': 'p', 'last_page': 38}, {'letter': 'q', 'last_page': 3}, {'letter': 'r', 'last_page': 21}, {'letter': 's', 'last_page': 51}, {'letter': 't', 'last_page': 24}, {'letter': 'u', 'last_page': 5}, {'letter': 'v', 'last_page': 8}, {'letter': 'w', 'last_page': 12}, {'letter': 'x', 'last_page': 1}, {'letter': 'y', 'last_page': 2}, {'letter': 'z', 'last_page': 1})

base_url = "https://japanesedictionary.org/browse/letter/{letter}/page-{page_number}"
link_folder_path = "links"
letter_links_folder_path = (link_folder_path+"/{letter_name}")


def worker(work_data):
    letter_name = work_data['letter']
    parent_folder = letter_links_folder_path.format(letter_name=letter_name)
    os.mkdir(parent_folder)
    for page_number in range(int(work_data["last_page"])):
        file_path = "{parent_folder_name}/{page_number}.txt".format(
            page_number=page_number+1, parent_folder_name=parent_folder)
        url = base_url.format(
            letter=work_data["letter"], page_number=page_number)
        with open(file_path, 'w+') as file:
            data = url
            file.write(data+'\n')


def wordFetch():
    path = link_folder_path
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        shutil.rmtree(path)
        os.makedirs(path)
    p = mp.Pool(26)
    p.map(worker, arguments)
