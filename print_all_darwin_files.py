"""Utility / helper script for printing all Darwin index folders"""

import os


def print_darwin_index_folders_list():

    abs_path = os.path.abspath("./darwin_indices")

    all_index_folders = os.listdir(abs_path)

    # Fit formatting of loader call
    parent_path = "/darwin_indices/"
    folder_index = 1
    for folder in all_index_folders:
        print(f'storage_folder{folder_index} = "{parent_path}{folder}"')
        folder_index += 1

def create_storage_folder_shorthand_list(end_index, start_index=1):
    for ind in range(start_index, end_index + 1):
        print(f"storage_folder{ind},")

def create_load_index_list(end_index, start_index=1):
    for ind in range(start_index, end_index + 1):
        print(f"index{ind} = load_index(storage_folder{ind})")

def print_index_shorthands_list(end_index, start_index=1):
    for ind in range(start_index, end_index + 1):
        print(f"index{ind},")

def print_chunk_list(end_index, start_index=1):
    for ind in range(start_index, end_index + 1):
        print(f"\"chunk{ind}\",")

if __name__ == "__main__":
    #print_darwin_index_folders_list()
    #create_storage_folder_shorthand_list(end_index=778, start_index=1)
    #create_load_index_list(end_index=778, start_index=1)
    #print_index_shorthands_list(end_index=778, start_index=1)
    print_chunk_list(end_index=778, start_index=1)