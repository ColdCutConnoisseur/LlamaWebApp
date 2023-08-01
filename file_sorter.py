"""Utility script to help sort Darwin PDFs parent folders into subfolders"""

import os
import sys

SIZE_CUTOFF = 70000000     # 70MB

class NewFolderTracker:
    def __init__(self, first_file, size_of_first_file):
        self.file_paths = [first_file]
        self.size = size_of_first_file

    def add_pdf_file(self, new_file_path, new_file_size):
        self.file_paths.append(new_file_path)
        self.size += new_file_size

        assert self.size <= SIZE_CUTOFF, "FILE container size too large!"


def sort_pdfs(folders_list, subfolder_start_index=1):
    abs_path = os.path.abspath("./DarwinPDFS")
    
    for parent_folder in folders_list:

        file_chunks = []

        base_path = f"{abs_path}/{parent_folder}/"
        pdf_files = [base_path + x for x in os.listdir(base_path) if os.path.isfile(base_path + x) and x != '.DS_Store']
        
        for file in pdf_files:
            file_size = os.path.getsize(file)
            
            # Find Files <= 70MB
            if file_size <= SIZE_CUTOFF:

                if len(file_chunks) > 0:
                    new_file_handled = False

                    for chunk in file_chunks:
                        if (chunk.size + file_size) <= SIZE_CUTOFF:
                            if not new_file_handled:
                                chunk.add_pdf_file(file, file_size)
                                new_file_handled = True

                    if not new_file_handled:
                        new_chunk = NewFolderTracker(file, file_size)
                        file_chunks.append(new_chunk)

                else: # First Chunk
                    new_chunk = NewFolderTracker(file, file_size)
                    file_chunks.append(new_chunk)

        subfolder_counter = subfolder_start_index
        for chunk in file_chunks:
            # Make new folder
            new_dir = base_path + f"subfolder{subfolder_counter}"
            os.mkdir(new_dir)

            for mv_file in chunk.file_paths:
                base = os.path.basename(mv_file)
                new_loc = new_dir + '/' + base
                os.rename(mv_file, new_dir + '/' + base)
                print(mv_file)
                print(new_loc)

            subfolder_counter += 1


if __name__ == "__main__":
    PARENT_FOLDERS_LIST = [
        "PDFs_24"
    ]
    
    sort_pdfs(PARENT_FOLDERS_LIST, subfolder_start_index=9)