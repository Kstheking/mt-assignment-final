import os


base_url = 'https://japanesedictionary.org/'

letter_list = ({'letter': 'a', 'page_count': 38}, {'letter': 'b', 'page_count': 25}, {'letter': 'c', 'page_count': 46}, {'letter': 'd', 'page_count': 25}, {
    'letter': 'e', 'page_count': 19}, {'letter': 'f', 'page_count': 21}, {'letter': 'g', 'page_count': 15}, {'letter': 'h', 'page_count': 17}, {'letter': 'i', 'page_count': 22}, {'letter': 'j', 'page_count': 4}, {'letter': 'k', 'page_count': 3}, {'letter': 'l', 'page_count': 14}, {'letter': 'm', 'page_count': 23}, {'letter': 'n', 'page_count': 9}, {'letter': 'o', 'page_count': 10}, {'letter': 'p', 'page_count': 38}, {'letter': 'q', 'page_count': 3}, {'letter': 'r', 'page_count': 21}, {'letter': 's', 'page_count': 51}, {'letter': 't', 'page_count': 24}, {'letter': 'u', 'page_count': 5}, {'letter': 'v', 'page_count': 8}, {'letter': 'w', 'page_count': 12}, {'letter': 'x', 'page_count': 1}, {'letter': 'y', 'page_count': 2}, {'letter': 'z', 'page_count': 1})

link_folder_path = 'links'


def get_subfolders(path):
    list_subfolders_path = [
        {'path': f.path, "name": f.name} for f in os.scandir(path) if f.is_dir()]
    return list_subfolders_path


def get_subfiles(path):
    list_subfiles_path = [
        {'path': f.path, 'name': f.name} for f in os.scandir(path) if f.is_file()]
    return list_subfiles_path
