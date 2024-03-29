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

def create_darwin_load_dict(indices_list, start_index=0):
    loaded_chunk_dict = {}

    for ind, index in enumerate(indices_list):
        actual_index = start_index+ind
        chunk_str = "chunk" + str(actual_index)
        loaded_index = load_index(index)
        loaded_chunk_dict[chunk_str] = loaded_index
        print(actual_index)

    return loaded_chunk_dict

def combine_darwin_indices(combined_dictionary):
    loaded_indices = list(combined_dictionary.values())
    summaries = list(combined_dictionary.keys())

    service_context = ServiceContext.from_defaults(chunk_size=512)
    storage_context = StorageContext.from_defaults()

    graph = ComposableGraph.from_indices(
                                    ListIndex,
                                    loaded_indices,
                                    index_summaries=summaries,
                                    service_context=service_context,
                                    storage_context=storage_context
                                    )
    
    return graph

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


INDICES_PATHS = [
        "/darwin_indices/darwin11_13",
        "/darwin_indices/darwin7_42",
        "/darwin_indices/darwin21_24",
        "/darwin_indices/darwin12_34",
        "/darwin_indices/darwin15_23",
        "/darwin_indices/darwin8_35",
        "/darwin_indices/darwin21_4",
        "/darwin_indices/darwin15_24",
        "/darwin_indices/darwin21_23",
        "/darwin_indices/darwin12_33",
        "/darwin_indices/darwin11_14",
        "/darwin_indices/darwin21_3",
        "/darwin_indices/darwin8_32",
        "/darwin_indices/darwin15_12",
        "/darwin_indices/darwin21_15",
        "/darwin_indices/darwin11_22",
        "/darwin_indices/darwin11_25",
        "/darwin_indices/darwin16_32",
        "/darwin_indices/darwin21_12",
        "/darwin_indices/darwin15_15",
        "/darwin_indices/darwin19_11",
        "/darwin_indices/darwin4_38",
        "/darwin_indices/darwin7_20",
        "/darwin_indices/darwin3_10",
        "/darwin_indices/darwin15_41",
        "/darwin_indices/darwin3_28",
        "/darwin_indices/darwin7_18",
        "/darwin_indices/darwin3_17",
        "/darwin_indices/darwin19_29",
        "/darwin_indices/darwin7_27",
        "/darwin_indices/darwin19_20",
        "/darwin_indices/darwin4_36",
        "/darwin_indices/darwin3_21",
        "/darwin_indices/darwin7_11",
        "/darwin_indices/darwin7_29",
        "/darwin_indices/darwin19_27",
        "/darwin_indices/darwin3_19",
        "/darwin_indices/darwin19_18",
        "/darwin_indices/darwin7_16",
        "/darwin_indices/darwin3_26",
        "/darwin_indices/darwin4_31",
        "/darwin_indices/darwin15_14",
        "/darwin_indices/darwin21_13",
        "/darwin_indices/darwin11_24",
        "/darwin_indices/darwin11_23",
        "/darwin_indices/darwin21_14",
        "/darwin_indices/darwin15_13",
        "/darwin_indices/darwin11_15",
        "/darwin_indices/darwin21_22",
        "/darwin_indices/darwin12_32",
        "/darwin_indices/darwin15_25",
        "/darwin_indices/darwin8_33",
        "/darwin_indices/darwin21_2",
        "/darwin_indices/darwin15_22",
        "/darwin_indices/darwin21_25",
        "/darwin_indices/darwin12_35",
        "/darwin_indices/darwin7_43",
        "/darwin_indices/darwin21_5",
        "/darwin_indices/darwin8_34",
        "/darwin_indices/darwin7_28",
        "/darwin_indices/darwin19_26",
        "/darwin_indices/darwin4_30",
        "/darwin_indices/darwin3_27",
        "/darwin_indices/darwin19_19",
        "/darwin_indices/darwin7_17",
        "/darwin_indices/darwin7_10",
        "/darwin_indices/darwin3_20",
        "/darwin_indices/darwin4_37",
        "/darwin_indices/darwin7_19",
        "/darwin_indices/darwin19_17",
        "/darwin_indices/darwin3_29",
        "/darwin_indices/darwin19_28",
        "/darwin_indices/darwin7_26",
        "/darwin_indices/darwin3_16",
        "/darwin_indices/darwin4_39",
        "/darwin_indices/darwin19_10",
        "/darwin_indices/darwin3_11",
        "/darwin_indices/darwin15_40",
        "/darwin_indices/darwin7_21",
        "/darwin_indices/darwin14_14",
        "/darwin_indices/darwin10_24",
        "/darwin_indices/darwin10_23",
        "/darwin_indices/darwin14_13",
        "/darwin_indices/darwin9_9",
        "/darwin_indices/darwin3_7",
        "/darwin_indices/darwin12_7",
        "/darwin_indices/darwin6_44",
        "/darwin_indices/darwin10_15",
        "/darwin_indices/darwin14_25",
        "/darwin_indices/darwin13_32",
        "/darwin_indices/darwin20_22",
        "/darwin_indices/darwin1_3",
        "/darwin_indices/darwin9_33",
        "/darwin_indices/darwin10_3",
        "/darwin_indices/darwin13_35",
        "/darwin_indices/darwin20_25",
        "/darwin_indices/darwin14_22",
        "/darwin_indices/darwin12_9",
        "/darwin_indices/darwin10_12",
        "/darwin_indices/darwin6_43",
        "/darwin_indices/darwin9_7",
        "/darwin_indices/darwin3_9",
        "/darwin_indices/darwin10_4",
        "/darwin_indices/darwin1_4",
        "/darwin_indices/darwin9_34",
        "/darwin_indices/darwin2_18",
        "/darwin_indices/darwin16_6",
        "/darwin_indices/darwin6_28",
        "/darwin_indices/darwin7_6",
        "/darwin_indices/darwin18_26",
        "/darwin_indices/darwin2_27",
        "/darwin_indices/darwin5_30",
        "/darwin_indices/darwin18_19",
        "/darwin_indices/darwin6_17",
        "/darwin_indices/darwin18_21",
        "/darwin_indices/darwin7_1",
        "/darwin_indices/darwin16_1",
        "/darwin_indices/darwin6_10",
        "/darwin_indices/darwin10_41",
        "/darwin_indices/darwin2_20",
        "/darwin_indices/darwin6_19",
        "/darwin_indices/darwin5_5",
        "/darwin_indices/darwin18_17",
        "/darwin_indices/darwin2_29",
        "/darwin_indices/darwin14_5",
        "/darwin_indices/darwin7_8",
        "/darwin_indices/darwin18_28",
        "/darwin_indices/darwin6_26",
        "/darwin_indices/darwin1_31",
        "/darwin_indices/darwin20_40",
        "/darwin_indices/darwin16_8",
        "/darwin_indices/darwin2_16",
        "/darwin_indices/darwin14_2",
        "/darwin_indices/darwin5_2",
        "/darwin_indices/darwin18_10",
        "/darwin_indices/darwin2_11",
        "/darwin_indices/darwin14_40",
        "/darwin_indices/darwin6_21",
        "/darwin_indices/darwin10_13",
        "/darwin_indices/darwin3_8",
        "/darwin_indices/darwin6_42",
        "/darwin_indices/darwin9_6",
        "/darwin_indices/darwin14_23",
        "/darwin_indices/darwin13_34",
        "/darwin_indices/darwin20_24",
        "/darwin_indices/darwin18_6",
        "/darwin_indices/darwin12_8",
        "/darwin_indices/darwin1_5",
        "/darwin_indices/darwin9_35",
        "/darwin_indices/darwin10_5",
        "/darwin_indices/darwin18_1",
        "/darwin_indices/darwin13_33",
        "/darwin_indices/darwin20_23",
        "/darwin_indices/darwin14_24",
        "/darwin_indices/darwin9_1",
        "/darwin_indices/darwin10_14",
        "/darwin_indices/darwin10_2",
        "/darwin_indices/darwin1_2",
        "/darwin_indices/darwin9_32",
        "/darwin_indices/darwin20_15",
        "/darwin_indices/darwin14_12",
        "/darwin_indices/darwin10_22",
        "/darwin_indices/darwin17_35",
        "/darwin_indices/darwin12_6",
        "/darwin_indices/darwin3_6",
        "/darwin_indices/darwin9_8",
        "/darwin_indices/darwin17_32",
        "/darwin_indices/darwin10_25",
        "/darwin_indices/darwin14_15",
        "/darwin_indices/darwin20_12",
        "/darwin_indices/darwin3_1",
        "/darwin_indices/darwin5_3",
        "/darwin_indices/darwin18_11",
        "/darwin_indices/darwin14_3",
        "/darwin_indices/darwin6_20",
        "/darwin_indices/darwin2_10",
        "/darwin_indices/darwin14_41",
        "/darwin_indices/darwin2_28",
        "/darwin_indices/darwin14_4",
        "/darwin_indices/darwin6_18",
        "/darwin_indices/darwin5_4",
        "/darwin_indices/darwin18_16",
        "/darwin_indices/darwin16_9",
        "/darwin_indices/darwin2_17",
        "/darwin_indices/darwin18_29",
        "/darwin_indices/darwin7_9",
        "/darwin_indices/darwin1_30",
        "/darwin_indices/darwin6_27",
        "/darwin_indices/darwin18_20",
        "/darwin_indices/darwin2_21",
        "/darwin_indices/darwin6_11",
        "/darwin_indices/darwin10_40",
        "/darwin_indices/darwin6_29",
        "/darwin_indices/darwin18_27",
        "/darwin_indices/darwin7_7",
        "/darwin_indices/darwin2_19",
        "/darwin_indices/darwin16_7",
        "/darwin_indices/darwin18_18",
        "/darwin_indices/darwin6_16",
        "/darwin_indices/darwin5_31",
        "/darwin_indices/darwin2_26",
        "/darwin_indices/darwin1_23",
        "/darwin_indices/darwin6_34",
        "/darwin_indices/darwin5_13",
        "/darwin_indices/darwin5_14",
        "/darwin_indices/darwin6_33",
        "/darwin_indices/darwin1_24",
        "/darwin_indices/darwin5_22",
        "/darwin_indices/darwin1_12",
        "/darwin_indices/darwin18_34",
        "/darwin_indices/darwin1_15",
        "/darwin_indices/darwin2_32",
        "/darwin_indices/darwin5_25",
        "/darwin_indices/darwin18_33",
        "/darwin_indices/darwin9_21",
        "/darwin_indices/darwin10_38",
        "/darwin_indices/darwin20_30",
        "/darwin_indices/darwin13_20",
        "/darwin_indices/darwin14_37",
        "/darwin_indices/darwin13_18",
        "/darwin_indices/darwin17_28",
        "/darwin_indices/darwin9_26",
        "/darwin_indices/darwin14_30",
        "/darwin_indices/darwin20_37",
        "/darwin_indices/darwin13_27",
        "/darwin_indices/darwin9_19",
        "/darwin_indices/darwin17_17",
        "/darwin_indices/darwin14_39",
        "/darwin_indices/darwin9_10",
        "/darwin_indices/darwin20_7",
        "/darwin_indices/darwin13_11",
        "/darwin_indices/darwin17_21",
        "/darwin_indices/darwin10_36",
        "/darwin_indices/darwin17_19",
        "/darwin_indices/darwin9_17",
        "/darwin_indices/darwin20_39",
        "/darwin_indices/darwin13_29",
        "/darwin_indices/darwin9_28",
        "/darwin_indices/darwin10_31",
        "/darwin_indices/darwin17_26",
        "/darwin_indices/darwin13_16",
        "/darwin_indices/darwin5_24",
        "/darwin_indices/darwin1_14",
        "/darwin_indices/darwin18_32",
        "/darwin_indices/darwin1_13",
        "/darwin_indices/darwin5_23",
        "/darwin_indices/darwin18_35",
        "/darwin_indices/darwin1_25",
        "/darwin_indices/darwin6_32",
        "/darwin_indices/darwin5_15",
        "/darwin_indices/darwin5_12",
        "/darwin_indices/darwin6_35",
        "/darwin_indices/darwin1_22",
        "/darwin_indices/darwin20_38",
        "/darwin_indices/darwin13_28",
        "/darwin_indices/darwin17_18",
        "/darwin_indices/darwin9_16",
        "/darwin_indices/darwin20_1",
        "/darwin_indices/darwin13_17",
        "/darwin_indices/darwin9_29",
        "/darwin_indices/darwin17_27",
        "/darwin_indices/darwin10_30",
        "/darwin_indices/darwin9_11",
        "/darwin_indices/darwin14_38",
        "/darwin_indices/darwin10_37",
        "/darwin_indices/darwin17_20",
        "/darwin_indices/darwin13_10",
        "/darwin_indices/darwin17_29",
        "/darwin_indices/darwin9_27",
        "/darwin_indices/darwin13_19",
        "/darwin_indices/darwin9_18",
        "/darwin_indices/darwin17_16",
        "/darwin_indices/darwin20_36",
        "/darwin_indices/darwin13_26",
        "/darwin_indices/darwin14_31",
        "/darwin_indices/darwin9_20",
        "/darwin_indices/darwin10_39",
        "/darwin_indices/darwin14_36",
        "/darwin_indices/darwin20_31",
        "/darwin_indices/darwin13_21",
        "/darwin_indices/darwin17_11",
        "/darwin_indices/darwin20_8",
        "/darwin_indices/darwin3_33",
        "/darwin_indices/darwin4_24",
        "/darwin_indices/darwin4_6",
        "/darwin_indices/darwin15_6",
        "/darwin_indices/darwin19_32",
        "/darwin_indices/darwin4_23",
        "/darwin_indices/darwin3_34",
        "/darwin_indices/darwin19_35",
        "/darwin_indices/darwin15_1",
        "/darwin_indices/darwin4_1",
        "/darwin_indices/darwin7_32",
        "/darwin_indices/darwin4_15",
        "/darwin_indices/darwin4_8",
        "/darwin_indices/darwin17_5",
        "/darwin_indices/darwin6_5",
        "/darwin_indices/darwin4_12",
        "/darwin_indices/darwin7_35",
        "/darwin_indices/darwin6_2",
        "/darwin_indices/darwin17_2",
        "/darwin_indices/darwin12_28",
        "/darwin_indices/darwin21_38",
        "/darwin_indices/darwin16_18",
        "/darwin_indices/darwin8_16",
        "/darwin_indices/darwin4_46",
        "/darwin_indices/darwin8_3",
        "/darwin_indices/darwin12_17",
        "/darwin_indices/darwin8_29",
        "/darwin_indices/darwin11_30",
        "/darwin_indices/darwin16_27",
        "/darwin_indices/darwin8_11",
        "/darwin_indices/darwin11_7",
        "/darwin_indices/darwin15_38",
        "/darwin_indices/darwin19_4",
        "/darwin_indices/darwin16_20",
        "/darwin_indices/darwin11_37",
        "/darwin_indices/darwin12_10",
        "/darwin_indices/darwin4_41",
        "/darwin_indices/darwin13_3",
        "/darwin_indices/darwin16_29",
        "/darwin_indices/darwin8_27",
        "/darwin_indices/darwin12_19",
        "/darwin_indices/darwin2_3",
        "/darwin_indices/darwin8_18",
        "/darwin_indices/darwin16_16",
        "/darwin_indices/darwin15_31",
        "/darwin_indices/darwin12_26",
        "/darwin_indices/darwin21_36",
        "/darwin_indices/darwin2_4",
        "/darwin_indices/darwin8_20",
        "/darwin_indices/darwin13_4",
        "/darwin_indices/darwin12_21",
        "/darwin_indices/darwin21_31",
        "/darwin_indices/darwin15_36",
        "/darwin_indices/darwin16_11",
        "/darwin_indices/darwin11_9",
        "/darwin_indices/darwin7_34",
        "/darwin_indices/darwin4_13",
        "/darwin_indices/darwin17_3",
        "/darwin_indices/darwin6_3",
        "/darwin_indices/darwin4_9",
        "/darwin_indices/darwin4_14",
        "/darwin_indices/darwin7_33",
        "/darwin_indices/darwin6_4",
        "/darwin_indices/darwin17_4",
        "/darwin_indices/darwin3_35",
        "/darwin_indices/darwin4_22",
        "/darwin_indices/darwin19_34",
        "/darwin_indices/darwin4_25",
        "/darwin_indices/darwin3_32",
        "/darwin_indices/darwin15_7",
        "/darwin_indices/darwin19_33",
        "/darwin_indices/darwin4_7",
        "/darwin_indices/darwin8_21",
        "/darwin_indices/darwin13_5",
        "/darwin_indices/darwin2_5",
        "/darwin_indices/darwin11_8",
        "/darwin_indices/darwin15_37",
        "/darwin_indices/darwin12_20",
        "/darwin_indices/darwin21_30",
        "/darwin_indices/darwin2_2",
        "/darwin_indices/darwin12_18",
        "/darwin_indices/darwin16_28",
        "/darwin_indices/darwin13_2",
        "/darwin_indices/darwin8_26",
        "/darwin_indices/darwin12_27",
        "/darwin_indices/darwin21_37",
        "/darwin_indices/darwin15_30",
        "/darwin_indices/darwin8_19",
        "/darwin_indices/darwin16_17",
        "/darwin_indices/darwin15_39",
        "/darwin_indices/darwin8_10",
        "/darwin_indices/darwin11_6",
        "/darwin_indices/darwin8_5",
        "/darwin_indices/darwin12_11",
        "/darwin_indices/darwin4_40",
        "/darwin_indices/darwin11_36",
        "/darwin_indices/darwin19_5",
        "/darwin_indices/darwin16_21",
        "/darwin_indices/darwin16_19",
        "/darwin_indices/darwin11_1",
        "/darwin_indices/darwin8_17",
        "/darwin_indices/darwin12_29",
        "/darwin_indices/darwin21_39",
        "/darwin_indices/darwin8_28",
        "/darwin_indices/darwin16_26",
        "/darwin_indices/darwin11_31",
        "/darwin_indices/darwin4_47",
        "/darwin_indices/darwin8_2",
        "/darwin_indices/darwin12_16",
        "/darwin_indices/darwin3_14",
        "/darwin_indices/darwin7_24",
        "/darwin_indices/darwin19_12",
        "/darwin_indices/darwin7_23",
        "/darwin_indices/darwin3_13",
        "/darwin_indices/darwin15_42",
        "/darwin_indices/darwin19_24",
        "/darwin_indices/darwin7_15",
        "/darwin_indices/darwin4_32",
        "/darwin_indices/darwin3_25",
        "/darwin_indices/darwin19_23",
        "/darwin_indices/darwin3_22",
        "/darwin_indices/darwin4_35",
        "/darwin_indices/darwin7_12",
        "/darwin_indices/darwin21_20",
        "/darwin_indices/darwin12_30",
        "/darwin_indices/darwin15_27",
        "/darwin_indices/darwin11_17",
        "/darwin_indices/darwin15_18",
        "/darwin_indices/darwin11_28",
        "/darwin_indices/darwin8_31",
        "/darwin_indices/darwin11_10",
        "/darwin_indices/darwin7_41",
        "/darwin_indices/darwin15_20",
        "/darwin_indices/darwin21_27",
        "/darwin_indices/darwin12_37",
        "/darwin_indices/darwin8_36",
        "/darwin_indices/darwin21_18",
        "/darwin_indices/darwin21_7",
        "/darwin_indices/darwin16_31",
        "/darwin_indices/darwin11_26",
        "/darwin_indices/darwin15_16",
        "/darwin_indices/darwin21_11",
        "/darwin_indices/darwin11_19",
        "/darwin_indices/darwin15_29",
        "/darwin_indices/darwin21_16",
        "/darwin_indices/darwin15_11",
        "/darwin_indices/darwin21_9",
        "/darwin_indices/darwin11_21",
        "/darwin_indices/darwin8_38",
        "/darwin_indices/darwin21_29",
        "/darwin_indices/darwin12_39",
        "/darwin_indices/darwin19_22",
        "/darwin_indices/darwin7_13",
        "/darwin_indices/darwin4_34",
        "/darwin_indices/darwin3_23",
        "/darwin_indices/darwin19_25",
        "/darwin_indices/darwin3_24",
        "/darwin_indices/darwin4_33",
        "/darwin_indices/darwin7_14",
        "/darwin_indices/darwin19_13",
        "/darwin_indices/darwin3_12",
        "/darwin_indices/darwin15_43",
        "/darwin_indices/darwin7_22",
        "/darwin_indices/darwin19_14",
        "/darwin_indices/darwin7_25",
        "/darwin_indices/darwin15_44",
        "/darwin_indices/darwin3_15",
        "/darwin_indices/darwin11_20",
        "/darwin_indices/darwin15_10",
        "/darwin_indices/darwin21_8",
        "/darwin_indices/darwin21_17",
        "/darwin_indices/darwin21_28",
        "/darwin_indices/darwin12_38",
        "/darwin_indices/darwin21_10",
        "/darwin_indices/darwin15_17",
        "/darwin_indices/darwin11_27",
        "/darwin_indices/darwin16_30",
        "/darwin_indices/darwin15_28",
        "/darwin_indices/darwin11_18",
        "/darwin_indices/darwin21_26",
        "/darwin_indices/darwin12_36",
        "/darwin_indices/darwin15_21",
        "/darwin_indices/darwin11_11",
        "/darwin_indices/darwin7_40",
        "/darwin_indices/darwin21_6",
        "/darwin_indices/darwin21_19",
        "/darwin_indices/darwin8_37",
        "/darwin_indices/darwin11_16",
        "/darwin_indices/darwin15_26",
        "/darwin_indices/darwin21_21",
        "/darwin_indices/darwin12_31",
        "/darwin_indices/darwin11_29",
        "/darwin_indices/darwin8_30",
        "/darwin_indices/darwin15_19",
        "/darwin_indices/darwin21_1",
        "/darwin_indices/darwin7_2",
        "/darwin_indices/darwin18_22",
        "/darwin_indices/darwin16_2",
        "/darwin_indices/darwin6_13",
        "/darwin_indices/darwin10_42",
        "/darwin_indices/darwin2_23",
        "/darwin_indices/darwin16_5",
        "/darwin_indices/darwin18_25",
        "/darwin_indices/darwin7_5",
        "/darwin_indices/darwin14_8",
        "/darwin_indices/darwin5_33",
        "/darwin_indices/darwin2_24",
        "/darwin_indices/darwin5_8",
        "/darwin_indices/darwin6_14",
        "/darwin_indices/darwin14_1",
        "/darwin_indices/darwin5_1",
        "/darwin_indices/darwin2_12",
        "/darwin_indices/darwin14_43",
        "/darwin_indices/darwin6_22",
        "/darwin_indices/darwin5_6",
        "/darwin_indices/darwin18_14",
        "/darwin_indices/darwin14_6",
        "/darwin_indices/darwin1_32",
        "/darwin_indices/darwin6_25",
        "/darwin_indices/darwin14_44",
        "/darwin_indices/darwin2_15",
        "/darwin_indices/darwin10_20",
        "/darwin_indices/darwin1_9",
        "/darwin_indices/darwin9_39",
        "/darwin_indices/darwin20_17",
        "/darwin_indices/darwin14_10",
        "/darwin_indices/darwin10_9",
        "/darwin_indices/darwin3_4",
        "/darwin_indices/darwin12_4",
        "/darwin_indices/darwin20_28",
        "/darwin_indices/darwin14_17",
        "/darwin_indices/darwin17_30",
        "/darwin_indices/darwin10_27",
        "/darwin_indices/darwin14_28",
        "/darwin_indices/darwin10_18",
        "/darwin_indices/darwin3_3",
        "/darwin_indices/darwin14_21",
        "/darwin_indices/darwin20_26",
        "/darwin_indices/darwin18_4",
        "/darwin_indices/darwin10_11",
        "/darwin_indices/darwin6_40",
        "/darwin_indices/darwin9_4",
        "/darwin_indices/darwin10_7",
        "/darwin_indices/darwin20_19",
        "/darwin_indices/darwin1_7",
        "/darwin_indices/darwin9_37",
        "/darwin_indices/darwin9_3",
        "/darwin_indices/darwin10_16",
        "/darwin_indices/darwin18_3",
        "/darwin_indices/darwin13_31",
        "/darwin_indices/darwin20_21",
        "/darwin_indices/darwin14_26",
        "/darwin_indices/darwin10_29",
        "/darwin_indices/darwin9_30",
        "/darwin_indices/darwin14_19",
        "/darwin_indices/darwin14_7",
        "/darwin_indices/darwin5_7",
        "/darwin_indices/darwin18_15",
        "/darwin_indices/darwin14_45",
        "/darwin_indices/darwin2_14",
        "/darwin_indices/darwin6_24",
        "/darwin_indices/darwin1_33",
        "/darwin_indices/darwin6_23",
        "/darwin_indices/darwin2_13",
        "/darwin_indices/darwin14_42",
        "/darwin_indices/darwin7_4",
        "/darwin_indices/darwin18_24",
        "/darwin_indices/darwin16_4",
        "/darwin_indices/darwin5_9",
        "/darwin_indices/darwin10_44",
        "/darwin_indices/darwin6_15",
        "/darwin_indices/darwin14_9",
        "/darwin_indices/darwin2_25",
        "/darwin_indices/darwin5_32",
        "/darwin_indices/darwin16_3",
        "/darwin_indices/darwin18_23",
        "/darwin_indices/darwin7_3",
        "/darwin_indices/darwin2_22",
        "/darwin_indices/darwin6_12",
        "/darwin_indices/darwin10_43",
        "/darwin_indices/darwin14_27",
        "/darwin_indices/darwin13_30",
        "/darwin_indices/darwin20_20",
        "/darwin_indices/darwin10_17",
        "/darwin_indices/darwin14_18",
        "/darwin_indices/darwin10_1",
        "/darwin_indices/darwin10_28",
        "/darwin_indices/darwin9_31",
        "/darwin_indices/darwin10_10",
        "/darwin_indices/darwin6_41",
        "/darwin_indices/darwin9_5",
        "/darwin_indices/darwin20_27",
        "/darwin_indices/darwin14_20",
        "/darwin_indices/darwin18_5",
        "/darwin_indices/darwin1_6",
        "/darwin_indices/darwin9_36",
        "/darwin_indices/darwin10_6",
        "/darwin_indices/darwin20_18",
        "/darwin_indices/darwin10_26",
        "/darwin_indices/darwin17_31",
        "/darwin_indices/darwin20_11",
        "/darwin_indices/darwin10_19",
        "/darwin_indices/darwin3_2",
        "/darwin_indices/darwin14_29",
        "/darwin_indices/darwin12_2",
        "/darwin_indices/darwin14_11",
        "/darwin_indices/darwin10_8",
        "/darwin_indices/darwin10_21",
        "/darwin_indices/darwin1_8",
        "/darwin_indices/darwin9_38",
        "/darwin_indices/darwin12_5",
        "/darwin_indices/darwin20_29",
        "/darwin_indices/darwin3_5",
        "/darwin_indices/darwin9_25",
        "/darwin_indices/darwin20_34",
        "/darwin_indices/darwin13_24",
        "/darwin_indices/darwin14_33",
        "/darwin_indices/darwin17_14",
        "/darwin_indices/darwin9_22",
        "/darwin_indices/darwin17_13",
        "/darwin_indices/darwin14_34",
        "/darwin_indices/darwin20_33",
        "/darwin_indices/darwin13_23",
        "/darwin_indices/darwin9_14",
        "/darwin_indices/darwin20_3",
        "/darwin_indices/darwin17_25",
        "/darwin_indices/darwin10_32",
        "/darwin_indices/darwin13_15",
        "/darwin_indices/darwin20_4",
        "/darwin_indices/darwin9_13",
        "/darwin_indices/darwin13_12",
        "/darwin_indices/darwin10_35",
        "/darwin_indices/darwin17_22",
        "/darwin_indices/darwin5_17",
        "/darwin_indices/darwin1_27",
        "/darwin_indices/darwin6_30",
        "/darwin_indices/darwin5_28",
        "/darwin_indices/darwin1_18",
        "/darwin_indices/darwin6_37",
        "/darwin_indices/darwin1_20",
        "/darwin_indices/darwin5_10",
        "/darwin_indices/darwin9_40",
        "/darwin_indices/darwin1_16",
        "/darwin_indices/darwin5_26",
        "/darwin_indices/darwin2_31",
        "/darwin_indices/darwin1_29",
        "/darwin_indices/darwin18_30",
        "/darwin_indices/darwin5_19",
        "/darwin_indices/darwin5_21",
        "/darwin_indices/darwin1_11",
        "/darwin_indices/darwin18_37",
        "/darwin_indices/darwin6_39",
        "/darwin_indices/darwin9_12",
        "/darwin_indices/darwin20_5",
        "/darwin_indices/darwin17_23",
        "/darwin_indices/darwin10_34",
        "/darwin_indices/darwin13_13",
        "/darwin_indices/darwin20_2",
        "/darwin_indices/darwin9_15",
        "/darwin_indices/darwin13_14",
        "/darwin_indices/darwin10_33",
        "/darwin_indices/darwin17_24",
        "/darwin_indices/darwin9_23",
        "/darwin_indices/darwin20_32",
        "/darwin_indices/darwin13_22",
        "/darwin_indices/darwin14_35",
        "/darwin_indices/darwin17_12",
        "/darwin_indices/darwin9_24",
        "/darwin_indices/darwin17_15",
        "/darwin_indices/darwin14_32",
        "/darwin_indices/darwin20_35",
        "/darwin_indices/darwin13_25",
        "/darwin_indices/darwin1_10",
        "/darwin_indices/darwin5_20",
        "/darwin_indices/darwin18_36",
        "/darwin_indices/darwin6_38",
        "/darwin_indices/darwin2_30",
        "/darwin_indices/darwin5_27",
        "/darwin_indices/darwin1_17",
        "/darwin_indices/darwin5_18",
        "/darwin_indices/darwin1_28",
        "/darwin_indices/darwin18_31",
        "/darwin_indices/darwin5_11",
        "/darwin_indices/darwin1_21",
        "/darwin_indices/darwin6_36",
        "/darwin_indices/darwin6_31",
        "/darwin_indices/darwin1_26",
        "/darwin_indices/darwin5_16",
        "/darwin_indices/darwin1_19",
        "/darwin_indices/darwin5_29",
        "/darwin_indices/darwin8_12",
        "/darwin_indices/darwin11_4",
        "/darwin_indices/darwin11_34",
        "/darwin_indices/darwin13_9",
        "/darwin_indices/darwin19_7",
        "/darwin_indices/darwin16_23",
        "/darwin_indices/darwin8_7",
        "/darwin_indices/darwin12_13",
        "/darwin_indices/darwin2_9",
        "/darwin_indices/darwin4_42",
        "/darwin_indices/darwin11_3",
        "/darwin_indices/darwin8_15",
        "/darwin_indices/darwin4_45",
        "/darwin_indices/darwin12_14",
        "/darwin_indices/darwin16_24",
        "/darwin_indices/darwin11_33",
        "/darwin_indices/darwin8_9",
        "/darwin_indices/darwin2_7",
        "/darwin_indices/darwin8_23",
        "/darwin_indices/darwin13_7",
        "/darwin_indices/darwin19_9",
        "/darwin_indices/darwin15_35",
        "/darwin_indices/darwin12_22",
        "/darwin_indices/darwin21_32",
        "/darwin_indices/darwin8_24",
        "/darwin_indices/darwin16_15",
        "/darwin_indices/darwin12_25",
        "/darwin_indices/darwin21_35",
        "/darwin_indices/darwin15_32",
        "/darwin_indices/darwin3_37",
        "/darwin_indices/darwin4_20",
        "/darwin_indices/darwin19_36",
        "/darwin_indices/darwin7_38",
        "/darwin_indices/darwin4_27",
        "/darwin_indices/darwin3_30",
        "/darwin_indices/darwin4_5",
        "/darwin_indices/darwin4_18",
        "/darwin_indices/darwin15_5",
        "/darwin_indices/darwin19_31",
        "/darwin_indices/darwin4_11",
        "/darwin_indices/darwin12_40",
        "/darwin_indices/darwin7_36",
        "/darwin_indices/darwin3_39",
        "/darwin_indices/darwin6_1",
        "/darwin_indices/darwin17_1",
        "/darwin_indices/darwin7_31",
        "/darwin_indices/darwin4_16",
        "/darwin_indices/darwin17_6",
        "/darwin_indices/darwin4_29",
        "/darwin_indices/darwin6_6",
        "/darwin_indices/darwin2_1",
        "/darwin_indices/darwin13_1",
        "/darwin_indices/darwin8_25",
        "/darwin_indices/darwin15_33",
        "/darwin_indices/darwin12_24",
        "/darwin_indices/darwin21_34",
        "/darwin_indices/darwin16_14",
        "/darwin_indices/darwin8_22",
        "/darwin_indices/darwin19_8",
        "/darwin_indices/darwin13_6",
        "/darwin_indices/darwin2_6",
        "/darwin_indices/darwin8_8",
        "/darwin_indices/darwin16_13",
        "/darwin_indices/darwin12_23",
        "/darwin_indices/darwin21_33",
        "/darwin_indices/darwin15_34",
        "/darwin_indices/darwin11_2",
        "/darwin_indices/darwin8_14",
        "/darwin_indices/darwin11_32",
        "/darwin_indices/darwin19_1",
        "/darwin_indices/darwin16_25",
        "/darwin_indices/darwin4_44",
        "/darwin_indices/darwin8_1",
        "/darwin_indices/darwin12_15",
        "/darwin_indices/darwin8_13",
        "/darwin_indices/darwin11_5",
        "/darwin_indices/darwin2_8",
        "/darwin_indices/darwin8_6",
        "/darwin_indices/darwin12_12",
        "/darwin_indices/darwin4_43",
        "/darwin_indices/darwin19_6",
        "/darwin_indices/darwin16_22",
        "/darwin_indices/darwin11_35",
        "/darwin_indices/darwin4_17",
        "/darwin_indices/darwin7_30",
        "/darwin_indices/darwin6_7",
        "/darwin_indices/darwin4_28",
        "/darwin_indices/darwin17_7",
        "/darwin_indices/darwin7_37",
        "/darwin_indices/darwin4_10",
        "/darwin_indices/darwin12_41",
        "/darwin_indices/darwin3_38",
        "/darwin_indices/darwin17_9",
        "/darwin_indices/darwin3_31",
        "/darwin_indices/darwin4_26",
        "/darwin_indices/darwin6_9",
        "/darwin_indices/darwin15_4",
        "/darwin_indices/darwin19_30",
        "/darwin_indices/darwin4_19",
        "/darwin_indices/darwin4_4",
        "/darwin_indices/darwin4_21",
        "/darwin_indices/darwin3_36",
        "/darwin_indices/darwin4_3",
        "/darwin_indices/darwin19_37",
        "/darwin_indices/darwin7_39",
        ]


def load_first_darwin_index_chunk():
    indices_to_load = INDICES_PATHS[:100]

    dict1 = create_darwin_load_dict(indices_to_load, start_index=0)
    print("Dict1 built!")

    return dict1

def load_second_darwin_index_chunk():
    indices_to_load = INDICES_PATHS[100:200]

    dict2 = create_darwin_load_dict(indices_to_load, start_index=100)
    print("Dict2 built!")

    return dict2

def load_third_darwin_index_chunk():
    indices_to_load = INDICES_PATHS[200:300]

    dict3 = create_darwin_load_dict(indices_to_load, start_index=200)
    print("Dict3 built!")

    return dict3

def load_fourth_darwin_index_chunk():
    indices_to_load = INDICES_PATHS[300:400]

    dict4 = create_darwin_load_dict(indices_to_load, start_index=300)
    print("Dict4 built!")

    return dict4

def load_fifth_darwin_index_chunk():
    indices_to_load = INDICES_PATHS[400:500]

    dict5 = create_darwin_load_dict(indices_to_load, start_index=400)
    print("Dict5 built!")

    return dict5

def load_sixth_darwin_index_chunk():
    indices_to_load = INDICES_PATHS[500:600]

    dict6 = create_darwin_load_dict(indices_to_load, start_index=500)
    print("Dict6 built!")

    return dict6

def load_seventh_darwin_index_chunk():
    indices_to_load = INDICES_PATHS[600:700]

    dict7 = create_darwin_load_dict(indices_to_load, start_index=600)
    print("Dict7 built!")

    return dict7

def load_eighth_darwin_index_chunk():
    indices_to_load = INDICES_PATHS[700:]

    dict8 = create_darwin_load_dict(indices_to_load, start_index=700)
    print("Dict8 built!")

    return dict8



if __name__ == "__main__":
    import os
    import config_file as cf

    os.environ['OPENAI_API_KEY'] = cf.OAI_KEY

    INDEX_DIRECTORY = cf.STORAGE_FOLDER

    if not INDEX_DIRECTORY:
        INDEX_DIRECTORY = "./storage"

    create_index(INDEX_DIRECTORY)
