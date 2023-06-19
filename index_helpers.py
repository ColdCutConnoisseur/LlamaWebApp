"""Supplemental functionality for creating and loading indices"""

import os

from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage, ServiceContext, ListIndex
from llama_index.indices.composability import ComposableGraph

def create_index(folder_to_index, save_index_directory):
    documents = SimpleDirectoryReader(folder_to_index).load_data()
    index = GPTVectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir=save_index_directory)
    print("Index successfully created and saved!")

def load_index(load_index_directory):
    abs_path = list(os.path.split(os.path.abspath(__file__)))[0]
    full_path = abs_path + load_index_directory
    storage_context = StorageContext.from_defaults(persist_dir=full_path)
    index = load_index_from_storage(storage_context)
    return index

def combine_pangolin_indices(storage_folder1, storage_folder2, storage_folder3, storage_folder4,
                             storage_folder5, storage_folder6, storage_folder7, storage_folder8,
                             storage_folder9, storage_folder10, storage_folder11, storage_folder12,
                             storage_folder13, storage_folder14, storage_folder15, storage_folder16,
                             storage_folder17, storage_folder18, storage_folder19, storage_folder20,
                             storage_folder21, storage_folder22, storage_folder23, storage_folder24,
                             storage_folder25, storage_folder26):
    service_context = ServiceContext.from_defaults(chunk_size=512)
    storage_context = StorageContext.from_defaults()

    index1 = load_index(storage_folder1)
    index2 = load_index(storage_folder2)
    index3 = load_index(storage_folder3)
    index4 = load_index(storage_folder4)
    index5 = load_index(storage_folder5)
    index6 = load_index(storage_folder6)
    index7 = load_index(storage_folder7)
    index8 = load_index(storage_folder8)
    index9 = load_index(storage_folder9)
    index10 = load_index(storage_folder10)
    index11 = load_index(storage_folder11)
    index12 = load_index(storage_folder12)
    index13 = load_index(storage_folder13)
    index14 = load_index(storage_folder14)
    index15 = load_index(storage_folder15)
    index16 = load_index(storage_folder16)
    index17 = load_index(storage_folder17)
    index18 = load_index(storage_folder18)
    index19 = load_index(storage_folder19)
    index20 = load_index(storage_folder20)
    index21 = load_index(storage_folder21)
    index22 = load_index(storage_folder22)
    index23 = load_index(storage_folder23)
    index24 = load_index(storage_folder24)
    index25 = load_index(storage_folder25)
    index26 = load_index(storage_folder26)

    graph = ComposableGraph.from_indices(
        ListIndex,
        [index1, index2, index3, index4, index5, index6, index7,
         index8, index9, index10, index11, index12, index13, index14,
         index15, index16, index17, index18, index19, index20, index21,
         index22, index23, index24, index25, index26],
        index_summaries=["chunk1", "chunk2", "chunk3", "chunk4", "chunk5",
                         "chunk6", "chunk7", "chunk8", "chunk9", "chunk10",
                         "chunk11", "chunk12", "chunk13", "chunk14", "chunk15",
                         "chunk16", "chunk17", "chunk18", "chunk19", "chunk20",
                         "chunk21", "chunk22", "chunk23", "chunk24", "chunk25",
                         "chunk26"],
        service_context=service_context,
        storage_context=storage_context
    )
    
    return graph


if __name__ == "__main__":
    import os
    import config_file as cf

    os.environ['OPENAI_API_KEY'] = cf.OAI_KEY

    INDEX_DIRECTORY = cf.STORAGE_FOLDER

    if not INDEX_DIRECTORY:
        INDEX_DIRECTORY = "./storage"

    create_index(INDEX_DIRECTORY)
