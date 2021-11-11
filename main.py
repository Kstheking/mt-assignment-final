
from common import csv_to_excel, json_to_csv_generator, meanings_folder_path

from words import fetch_words_link
from meaning import get_merged_meaning, fetch_meanings

csv_file_path = "english_to_japanease.csv"
excel_file_path = "english_to_japanease.xlsx"

if __name__ == '__main__':
    print("----------- words link fetching has started ---------------")
    fetch_words_link()
    print("----------- words link fetching has completed and words meaning fetching started  ---------------")
    fetch_meanings()
    print("----------- words meaning fetching has completed, words meaning merging has started  ---------------")
    data = get_merged_meaning()
    print("----------- words meaning merged successfully  ---------------")
    json_to_csv_generator(json_file_path=meanings_folder_path +
                          "/merged.json", csv_file_path=csv_file_path)
    csv_to_excel(csv_file_path, excel_file_path)
