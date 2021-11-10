
from common import csv_to_excel, json_to_csv_generator, meanings_folder_path

from words import fetch_words_link
from meaning import get_merged_meaning, fetch_meanings

csv_file_path = "english_to_japanease.csv"
excel_file_path = "english_to_japanease.xlsx"

if __name__ == '__main__':
    # fetch_words_link()
    # fetch_meanings()
    data = get_merged_meaning()
    json_to_csv_generator(json_file_path=meanings_folder_path +
                          "/merged.json", csv_file_path=csv_file_path)
    csv_to_excel(csv_file_path, excel_file_path)
