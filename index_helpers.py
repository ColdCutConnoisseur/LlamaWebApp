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

def combine_darwin_indices(storage_folder1,
                        storage_folder2,
                        storage_folder3,
                        storage_folder4,
                        storage_folder5,
                        storage_folder6,
                        storage_folder7,
                        storage_folder8,
                        storage_folder9,
                        storage_folder10,
                        storage_folder11,
                        storage_folder12,
                        storage_folder13,
                        storage_folder14,
                        storage_folder15,
                        storage_folder16,
                        storage_folder17,
                        storage_folder18,
                        storage_folder19,
                        storage_folder20,
                        storage_folder21,
                        storage_folder22,
                        storage_folder23,
                        storage_folder24,
                        storage_folder25,
                        storage_folder26,
                        storage_folder27,
                        storage_folder28,
                        storage_folder29,
                        storage_folder30,
                        storage_folder31,
                        storage_folder32,
                        storage_folder33,
                        storage_folder34,
                        storage_folder35,
                        storage_folder36,
                        storage_folder37,
                        storage_folder38,
                        storage_folder39,
                        storage_folder40,
                        storage_folder41,
                        storage_folder42,
                        storage_folder43,
                        storage_folder44,
                        storage_folder45,
                        storage_folder46,
                        storage_folder47,
                        storage_folder48,
                        storage_folder49,
                        storage_folder50,
                        storage_folder51,
                        storage_folder52,
                        storage_folder53,
                        storage_folder54,
                        storage_folder55,
                        storage_folder56,
                        storage_folder57,
                        storage_folder58,
                        storage_folder59,
                        storage_folder60,
                        storage_folder61,
                        storage_folder62,
                        storage_folder63,
                        storage_folder64,
                        storage_folder65,
                        storage_folder66,
                        storage_folder67,
                        storage_folder68,
                        storage_folder69,
                        storage_folder70,
                        storage_folder71,
                        storage_folder72,
                        storage_folder73,
                        storage_folder74,
                        storage_folder75,
                        storage_folder76,
                        storage_folder77,
                        storage_folder78,
                        storage_folder79,
                        storage_folder80,
                        storage_folder81,
                        storage_folder82,
                        storage_folder83,
                        storage_folder84,
                        storage_folder85,
                        storage_folder86,
                        storage_folder87,
                        storage_folder88,
                        storage_folder89,
                        storage_folder90,
                        storage_folder91,
                        storage_folder92,
                        storage_folder93,
                        storage_folder94,
                        storage_folder95,
                        storage_folder96,
                        storage_folder97,
                        storage_folder98,
                        storage_folder99,
                        storage_folder100,
                        storage_folder101,
                        storage_folder102,
                        storage_folder103,
                        storage_folder104,
                        storage_folder105,
                        storage_folder106,
                        storage_folder107,
                        storage_folder108,
                        storage_folder109,
                        storage_folder110,
                        storage_folder111,
                        storage_folder112,
                        storage_folder113,
                        storage_folder114,
                        storage_folder115,
                        storage_folder116,
                        storage_folder117,
                        storage_folder118,
                        storage_folder119,
                        storage_folder120,
                        storage_folder121,
                        storage_folder122,
                        storage_folder123,
                        storage_folder124,
                        storage_folder125,
                        storage_folder126,
                        storage_folder127,
                        storage_folder128,
                        storage_folder129,
                        storage_folder130,
                        storage_folder131,
                        storage_folder132,
                        storage_folder133,
                        storage_folder134,
                        storage_folder135,
                        storage_folder136,
                        storage_folder137,
                        storage_folder138,
                        storage_folder139,
                        storage_folder140,
                        storage_folder141,
                        storage_folder142,
                        storage_folder143,
                        storage_folder144,
                        storage_folder145,
                        storage_folder146,
                        storage_folder147,
                        storage_folder148,
                        storage_folder149,
                        storage_folder150,
                        storage_folder151,
                        storage_folder152,
                        storage_folder153,
                        storage_folder154,
                        storage_folder155,
                        storage_folder156,
                        storage_folder157,
                        storage_folder158,
                        storage_folder159,
                        storage_folder160,
                        storage_folder161,
                        storage_folder162,
                        storage_folder163,
                        storage_folder164,
                        storage_folder165,
                        storage_folder166,
                        storage_folder167,
                        storage_folder168,
                        storage_folder169,
                        storage_folder170,
                        storage_folder171,
                        storage_folder172,
                        storage_folder173,
                        storage_folder174,
                        storage_folder175,
                        storage_folder176,
                        storage_folder177,
                        storage_folder178,
                        storage_folder179,
                        storage_folder180,
                        storage_folder181,
                        storage_folder182,
                        storage_folder183,
                        storage_folder184,
                        storage_folder185,
                        storage_folder186,
                        storage_folder187,
                        storage_folder188,
                        storage_folder189,
                        storage_folder190,
                        storage_folder191,
                        storage_folder192,
                        storage_folder193,
                        storage_folder194,
                        storage_folder195,
                        storage_folder196,
                        storage_folder197,
                        storage_folder198,
                        storage_folder199,
                        storage_folder200,
                        storage_folder201,
                        storage_folder202,
                        storage_folder203,
                        storage_folder204,
                        storage_folder205,
                        storage_folder206,
                        storage_folder207,
                        storage_folder208,
                        storage_folder209,
                        storage_folder210,
                        storage_folder211,
                        storage_folder212,
                        storage_folder213,
                        storage_folder214,
                        storage_folder215,
                        storage_folder216,
                        storage_folder217,
                        storage_folder218,
                        storage_folder219,
                        storage_folder220,
                        storage_folder221,
                        storage_folder222,
                        storage_folder223,
                        storage_folder224,
                        storage_folder225,
                        storage_folder226,
                        storage_folder227,
                        storage_folder228,
                        storage_folder229,
                        storage_folder230,
                        storage_folder231,
                        storage_folder232,
                        storage_folder233,
                        storage_folder234,
                        storage_folder235,
                        storage_folder236,
                        storage_folder237,
                        storage_folder238,
                        storage_folder239,
                        storage_folder240,
                        storage_folder241,
                        storage_folder242,
                        storage_folder243,
                        storage_folder244,
                        storage_folder245,
                        storage_folder246,
                        storage_folder247,
                        storage_folder248,
                        storage_folder249,
                        storage_folder250,
                        storage_folder251,
                        storage_folder252,
                        storage_folder253,
                        storage_folder254,
                        storage_folder255,
                        storage_folder256,
                        storage_folder257,
                        storage_folder258,
                        storage_folder259,
                        storage_folder260,
                        storage_folder261,
                        storage_folder262,
                        storage_folder263,
                        storage_folder264,
                        storage_folder265,
                        storage_folder266,
                        storage_folder267,
                        storage_folder268,
                        storage_folder269,
                        storage_folder270,
                        storage_folder271,
                        storage_folder272,
                        storage_folder273,
                        storage_folder274,
                        storage_folder275,
                        storage_folder276,
                        storage_folder277,
                        storage_folder278,
                        storage_folder279,
                        storage_folder280,
                        storage_folder281,
                        storage_folder282,
                        storage_folder283,
                        storage_folder284,
                        storage_folder285,
                        storage_folder286,
                        storage_folder287,
                        storage_folder288,
                        storage_folder289,
                        storage_folder290,
                        storage_folder291,
                        storage_folder292,
                        storage_folder293,
                        storage_folder294,
                        storage_folder295,
                        storage_folder296,
                        storage_folder297,
                        storage_folder298,
                        storage_folder299,
                        storage_folder300,
                        storage_folder301,
                        storage_folder302,
                        storage_folder303,
                        storage_folder304,
                        storage_folder305,
                        storage_folder306,
                        storage_folder307,
                        storage_folder308,
                        storage_folder309,
                        storage_folder310,
                        storage_folder311,
                        storage_folder312,
                        storage_folder313,
                        storage_folder314,
                        storage_folder315,
                        storage_folder316,
                        storage_folder317,
                        storage_folder318,
                        storage_folder319,
                        storage_folder320,
                        storage_folder321,
                        storage_folder322,
                        storage_folder323,
                        storage_folder324,
                        storage_folder325,
                        storage_folder326,
                        storage_folder327,
                        storage_folder328,
                        storage_folder329,
                        storage_folder330,
                        storage_folder331,
                        storage_folder332,
                        storage_folder333,
                        storage_folder334,
                        storage_folder335,
                        storage_folder336,
                        storage_folder337,
                        storage_folder338,
                        storage_folder339,
                        storage_folder340,
                        storage_folder341,
                        storage_folder342,
                        storage_folder343,
                        storage_folder344,
                        storage_folder345,
                        storage_folder346,
                        storage_folder347,
                        storage_folder348,
                        storage_folder349,
                        storage_folder350,
                        storage_folder351,
                        storage_folder352,
                        storage_folder353,
                        storage_folder354,
                        storage_folder355,
                        storage_folder356,
                        storage_folder357,
                        storage_folder358,
                        storage_folder359,
                        storage_folder360,
                        storage_folder361,
                        storage_folder362,
                        storage_folder363,
                        storage_folder364,
                        storage_folder365,
                        storage_folder366,
                        storage_folder367,
                        storage_folder368,
                        storage_folder369,
                        storage_folder370,
                        storage_folder371,
                        storage_folder372,
                        storage_folder373,
                        storage_folder374,
                        storage_folder375,
                        storage_folder376,
                        storage_folder377,
                        storage_folder378,
                        storage_folder379,
                        storage_folder380,
                        storage_folder381,
                        storage_folder382,
                        storage_folder383,
                        storage_folder384,
                        storage_folder385,
                        storage_folder386,
                        storage_folder387,
                        storage_folder388,
                        storage_folder389,
                        storage_folder390,
                        storage_folder391,
                        storage_folder392,
                        storage_folder393,
                        storage_folder394,
                        storage_folder395,
                        storage_folder396,
                        storage_folder397,
                        storage_folder398,
                        storage_folder399,
                        storage_folder400,
                        storage_folder401,
                        storage_folder402,
                        storage_folder403,
                        storage_folder404,
                        storage_folder405,
                        storage_folder406,
                        storage_folder407,
                        storage_folder408,
                        storage_folder409,
                        storage_folder410,
                        storage_folder411,
                        storage_folder412,
                        storage_folder413,
                        storage_folder414,
                        storage_folder415,
                        storage_folder416,
                        storage_folder417,
                        storage_folder418,
                        storage_folder419,
                        storage_folder420,
                        storage_folder421,
                        storage_folder422,
                        storage_folder423,
                        storage_folder424,
                        storage_folder425,
                        storage_folder426,
                        storage_folder427,
                        storage_folder428,
                        storage_folder429,
                        storage_folder430,
                        storage_folder431,
                        storage_folder432,
                        storage_folder433,
                        storage_folder434,
                        storage_folder435,
                        storage_folder436,
                        storage_folder437,
                        storage_folder438,
                        storage_folder439,
                        storage_folder440,
                        storage_folder441,
                        storage_folder442,
                        storage_folder443,
                        storage_folder444,
                        storage_folder445,
                        storage_folder446,
                        storage_folder447,
                        storage_folder448,
                        storage_folder449,
                        storage_folder450,
                        storage_folder451,
                        storage_folder452,
                        storage_folder453,
                        storage_folder454,
                        storage_folder455,
                        storage_folder456,
                        storage_folder457,
                        storage_folder458,
                        storage_folder459,
                        storage_folder460,
                        storage_folder461,
                        storage_folder462,
                        storage_folder463,
                        storage_folder464,
                        storage_folder465,
                        storage_folder466,
                        storage_folder467,
                        storage_folder468,
                        storage_folder469,
                        storage_folder470,
                        storage_folder471,
                        storage_folder472,
                        storage_folder473,
                        storage_folder474,
                        storage_folder475,
                        storage_folder476,
                        storage_folder477,
                        storage_folder478,
                        storage_folder479,
                        storage_folder480,
                        storage_folder481,
                        storage_folder482,
                        storage_folder483,
                        storage_folder484,
                        storage_folder485,
                        storage_folder486,
                        storage_folder487,
                        storage_folder488,
                        storage_folder489,
                        storage_folder490,
                        storage_folder491,
                        storage_folder492,
                        storage_folder493,
                        storage_folder494,
                        storage_folder495,
                        storage_folder496,
                        storage_folder497,
                        storage_folder498,
                        storage_folder499,
                        storage_folder500,
                        storage_folder501,
                        storage_folder502,
                        storage_folder503,
                        storage_folder504,
                        storage_folder505,
                        storage_folder506,
                        storage_folder507,
                        storage_folder508,
                        storage_folder509,
                        storage_folder510,
                        storage_folder511,
                        storage_folder512,
                        storage_folder513,
                        storage_folder514,
                        storage_folder515,
                        storage_folder516,
                        storage_folder517,
                        storage_folder518,
                        storage_folder519,
                        storage_folder520,
                        storage_folder521,
                        storage_folder522,
                        storage_folder523,
                        storage_folder524,
                        storage_folder525,
                        storage_folder526,
                        storage_folder527,
                        storage_folder528,
                        storage_folder529,
                        storage_folder530,
                        storage_folder531,
                        storage_folder532,
                        storage_folder533,
                        storage_folder534,
                        storage_folder535,
                        storage_folder536,
                        storage_folder537,
                        storage_folder538,
                        storage_folder539,
                        storage_folder540,
                        storage_folder541,
                        storage_folder542,
                        storage_folder543,
                        storage_folder544,
                        storage_folder545,
                        storage_folder546,
                        storage_folder547,
                        storage_folder548,
                        storage_folder549,
                        storage_folder550,
                        storage_folder551,
                        storage_folder552,
                        storage_folder553,
                        storage_folder554,
                        storage_folder555,
                        storage_folder556,
                        storage_folder557,
                        storage_folder558,
                        storage_folder559,
                        storage_folder560,
                        storage_folder561,
                        storage_folder562,
                        storage_folder563,
                        storage_folder564,
                        storage_folder565,
                        storage_folder566,
                        storage_folder567,
                        storage_folder568,
                        storage_folder569,
                        storage_folder570,
                        storage_folder571,
                        storage_folder572,
                        storage_folder573,
                        storage_folder574,
                        storage_folder575,
                        storage_folder576,
                        storage_folder577,
                        storage_folder578,
                        storage_folder579,
                        storage_folder580,
                        storage_folder581,
                        storage_folder582,
                        storage_folder583,
                        storage_folder584,
                        storage_folder585,
                        storage_folder586,
                        storage_folder587,
                        storage_folder588,
                        storage_folder589,
                        storage_folder590,
                        storage_folder591,
                        storage_folder592,
                        storage_folder593,
                        storage_folder594,
                        storage_folder595,
                        storage_folder596,
                        storage_folder597,
                        storage_folder598,
                        storage_folder599,
                        storage_folder600,
                        storage_folder601,
                        storage_folder602,
                        storage_folder603,
                        storage_folder604,
                        storage_folder605,
                        storage_folder606,
                        storage_folder607,
                        storage_folder608,
                        storage_folder609,
                        storage_folder610,
                        storage_folder611,
                        storage_folder612,
                        storage_folder613,
                        storage_folder614,
                        storage_folder615,
                        storage_folder616,
                        storage_folder617,
                        storage_folder618,
                        storage_folder619,
                        storage_folder620,
                        storage_folder621,
                        storage_folder622,
                        storage_folder623,
                        storage_folder624,
                        storage_folder625,
                        storage_folder626,
                        storage_folder627,
                        storage_folder628,
                        storage_folder629,
                        storage_folder630,
                        storage_folder631,
                        storage_folder632,
                        storage_folder633,
                        storage_folder634,
                        storage_folder635,
                        storage_folder636,
                        storage_folder637,
                        storage_folder638,
                        storage_folder639,
                        storage_folder640,
                        storage_folder641,
                        storage_folder642,
                        storage_folder643,
                        storage_folder644,
                        storage_folder645,
                        storage_folder646,
                        storage_folder647,
                        storage_folder648,
                        storage_folder649,
                        storage_folder650,
                        storage_folder651,
                        storage_folder652,
                        storage_folder653,
                        storage_folder654,
                        storage_folder655,
                        storage_folder656,
                        storage_folder657,
                        storage_folder658,
                        storage_folder659,
                        storage_folder660,
                        storage_folder661,
                        storage_folder662,
                        storage_folder663,
                        storage_folder664,
                        storage_folder665,
                        storage_folder666,
                        storage_folder667,
                        storage_folder668,
                        storage_folder669,
                        storage_folder670,
                        storage_folder671,
                        storage_folder672,
                        storage_folder673,
                        storage_folder674,
                        storage_folder675,
                        storage_folder676,
                        storage_folder677,
                        storage_folder678,
                        storage_folder679,
                        storage_folder680,
                        storage_folder681,
                        storage_folder682,
                        storage_folder683,
                        storage_folder684,
                        storage_folder685,
                        storage_folder686,
                        storage_folder687,
                        storage_folder688,
                        storage_folder689,
                        storage_folder690,
                        storage_folder691,
                        storage_folder692,
                        storage_folder693,
                        storage_folder694,
                        storage_folder695,
                        storage_folder696,
                        storage_folder697,
                        storage_folder698,
                        storage_folder699,
                        storage_folder700,
                        storage_folder701,
                        storage_folder702,
                        storage_folder703,
                        storage_folder704,
                        storage_folder705,
                        storage_folder706,
                        storage_folder707,
                        storage_folder708,
                        storage_folder709,
                        storage_folder710,
                        storage_folder711,
                        storage_folder712,
                        storage_folder713,
                        storage_folder714,
                        storage_folder715,
                        storage_folder716,
                        storage_folder717,
                        storage_folder718,
                        storage_folder719,
                        storage_folder720,
                        storage_folder721,
                        storage_folder722,
                        storage_folder723,
                        storage_folder724,
                        storage_folder725,
                        storage_folder726,
                        storage_folder727,
                        storage_folder728,
                        storage_folder729,
                        storage_folder730,
                        storage_folder731,
                        storage_folder732,
                        storage_folder733,
                        storage_folder734,
                        storage_folder735,
                        storage_folder736,
                        storage_folder737,
                        storage_folder738,
                        storage_folder739,
                        storage_folder740,
                        storage_folder741,
                        storage_folder742,
                        storage_folder743,
                        storage_folder744,
                        storage_folder745,
                        storage_folder746,
                        storage_folder747,
                        storage_folder748,
                        storage_folder749,
                        storage_folder750,
                        storage_folder751,
                        storage_folder752,
                        storage_folder753,
                        storage_folder754,
                        storage_folder755,
                        storage_folder756,
                        storage_folder757,
                        storage_folder758,
                        storage_folder759,
                        storage_folder760,
                        storage_folder761,
                        storage_folder762,
                        storage_folder763,
                        storage_folder764,
                        storage_folder765,
                        storage_folder766,
                        storage_folder767,
                        storage_folder768,
                        storage_folder769,
                        storage_folder770,
                        storage_folder771,
                        storage_folder772,
                        storage_folder773,
                        storage_folder774,
                        storage_folder775,
                        storage_folder776,
                        storage_folder777,
                        storage_folder778):
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
    index27 = load_index(storage_folder27)
    index28 = load_index(storage_folder28)
    index29 = load_index(storage_folder29)
    index30 = load_index(storage_folder30)
    index31 = load_index(storage_folder31)
    index32 = load_index(storage_folder32)
    index33 = load_index(storage_folder33)
    index34 = load_index(storage_folder34)
    index35 = load_index(storage_folder35)
    index36 = load_index(storage_folder36)
    index37 = load_index(storage_folder37)
    index38 = load_index(storage_folder38)
    index39 = load_index(storage_folder39)
    index40 = load_index(storage_folder40)
    index41 = load_index(storage_folder41)
    index42 = load_index(storage_folder42)
    index43 = load_index(storage_folder43)
    index44 = load_index(storage_folder44)
    index45 = load_index(storage_folder45)
    index46 = load_index(storage_folder46)
    index47 = load_index(storage_folder47)
    index48 = load_index(storage_folder48)
    index49 = load_index(storage_folder49)
    index50 = load_index(storage_folder50)
    index51 = load_index(storage_folder51)
    index52 = load_index(storage_folder52)
    index53 = load_index(storage_folder53)
    index54 = load_index(storage_folder54)
    index55 = load_index(storage_folder55)
    index56 = load_index(storage_folder56)
    index57 = load_index(storage_folder57)
    index58 = load_index(storage_folder58)
    index59 = load_index(storage_folder59)
    index60 = load_index(storage_folder60)
    index61 = load_index(storage_folder61)
    index62 = load_index(storage_folder62)
    index63 = load_index(storage_folder63)
    index64 = load_index(storage_folder64)
    index65 = load_index(storage_folder65)
    index66 = load_index(storage_folder66)
    index67 = load_index(storage_folder67)
    index68 = load_index(storage_folder68)
    index69 = load_index(storage_folder69)
    index70 = load_index(storage_folder70)
    index71 = load_index(storage_folder71)
    index72 = load_index(storage_folder72)
    index73 = load_index(storage_folder73)
    index74 = load_index(storage_folder74)
    index75 = load_index(storage_folder75)
    index76 = load_index(storage_folder76)
    index77 = load_index(storage_folder77)
    index78 = load_index(storage_folder78)
    index79 = load_index(storage_folder79)
    index80 = load_index(storage_folder80)
    index81 = load_index(storage_folder81)
    index82 = load_index(storage_folder82)
    index83 = load_index(storage_folder83)
    index84 = load_index(storage_folder84)
    index85 = load_index(storage_folder85)
    index86 = load_index(storage_folder86)
    index87 = load_index(storage_folder87)
    index88 = load_index(storage_folder88)
    index89 = load_index(storage_folder89)
    index90 = load_index(storage_folder90)
    index91 = load_index(storage_folder91)
    index92 = load_index(storage_folder92)
    index93 = load_index(storage_folder93)
    index94 = load_index(storage_folder94)
    index95 = load_index(storage_folder95)
    index96 = load_index(storage_folder96)
    index97 = load_index(storage_folder97)
    index98 = load_index(storage_folder98)
    index99 = load_index(storage_folder99)
    index100 = load_index(storage_folder100)
    index101 = load_index(storage_folder101)
    index102 = load_index(storage_folder102)
    index103 = load_index(storage_folder103)
    index104 = load_index(storage_folder104)
    index105 = load_index(storage_folder105)
    index106 = load_index(storage_folder106)
    index107 = load_index(storage_folder107)
    index108 = load_index(storage_folder108)
    index109 = load_index(storage_folder109)
    index110 = load_index(storage_folder110)
    index111 = load_index(storage_folder111)
    index112 = load_index(storage_folder112)
    index113 = load_index(storage_folder113)
    index114 = load_index(storage_folder114)
    index115 = load_index(storage_folder115)
    index116 = load_index(storage_folder116)
    index117 = load_index(storage_folder117)
    index118 = load_index(storage_folder118)
    index119 = load_index(storage_folder119)
    index120 = load_index(storage_folder120)
    index121 = load_index(storage_folder121)
    index122 = load_index(storage_folder122)
    index123 = load_index(storage_folder123)
    index124 = load_index(storage_folder124)
    index125 = load_index(storage_folder125)
    index126 = load_index(storage_folder126)
    index127 = load_index(storage_folder127)
    index128 = load_index(storage_folder128)
    index129 = load_index(storage_folder129)
    index130 = load_index(storage_folder130)
    index131 = load_index(storage_folder131)
    index132 = load_index(storage_folder132)
    index133 = load_index(storage_folder133)
    index134 = load_index(storage_folder134)
    index135 = load_index(storage_folder135)
    index136 = load_index(storage_folder136)
    index137 = load_index(storage_folder137)
    index138 = load_index(storage_folder138)
    index139 = load_index(storage_folder139)
    index140 = load_index(storage_folder140)
    index141 = load_index(storage_folder141)
    index142 = load_index(storage_folder142)
    index143 = load_index(storage_folder143)
    index144 = load_index(storage_folder144)
    index145 = load_index(storage_folder145)
    index146 = load_index(storage_folder146)
    index147 = load_index(storage_folder147)
    index148 = load_index(storage_folder148)
    index149 = load_index(storage_folder149)
    index150 = load_index(storage_folder150)
    index151 = load_index(storage_folder151)
    index152 = load_index(storage_folder152)
    index153 = load_index(storage_folder153)
    index154 = load_index(storage_folder154)
    index155 = load_index(storage_folder155)
    index156 = load_index(storage_folder156)
    index157 = load_index(storage_folder157)
    index158 = load_index(storage_folder158)
    index159 = load_index(storage_folder159)
    index160 = load_index(storage_folder160)
    index161 = load_index(storage_folder161)
    index162 = load_index(storage_folder162)
    index163 = load_index(storage_folder163)
    index164 = load_index(storage_folder164)
    index165 = load_index(storage_folder165)
    index166 = load_index(storage_folder166)
    index167 = load_index(storage_folder167)
    index168 = load_index(storage_folder168)
    index169 = load_index(storage_folder169)
    index170 = load_index(storage_folder170)
    index171 = load_index(storage_folder171)
    index172 = load_index(storage_folder172)
    index173 = load_index(storage_folder173)
    index174 = load_index(storage_folder174)
    index175 = load_index(storage_folder175)
    index176 = load_index(storage_folder176)
    index177 = load_index(storage_folder177)
    index178 = load_index(storage_folder178)
    index179 = load_index(storage_folder179)
    index180 = load_index(storage_folder180)
    index181 = load_index(storage_folder181)
    index182 = load_index(storage_folder182)
    index183 = load_index(storage_folder183)
    index184 = load_index(storage_folder184)
    index185 = load_index(storage_folder185)
    index186 = load_index(storage_folder186)
    index187 = load_index(storage_folder187)
    index188 = load_index(storage_folder188)
    index189 = load_index(storage_folder189)
    index190 = load_index(storage_folder190)
    index191 = load_index(storage_folder191)
    index192 = load_index(storage_folder192)
    index193 = load_index(storage_folder193)
    index194 = load_index(storage_folder194)
    index195 = load_index(storage_folder195)
    index196 = load_index(storage_folder196)
    index197 = load_index(storage_folder197)
    index198 = load_index(storage_folder198)
    index199 = load_index(storage_folder199)
    index200 = load_index(storage_folder200)
    index201 = load_index(storage_folder201)
    index202 = load_index(storage_folder202)
    index203 = load_index(storage_folder203)
    index204 = load_index(storage_folder204)
    index205 = load_index(storage_folder205)
    index206 = load_index(storage_folder206)
    index207 = load_index(storage_folder207)
    index208 = load_index(storage_folder208)
    index209 = load_index(storage_folder209)
    index210 = load_index(storage_folder210)
    index211 = load_index(storage_folder211)
    index212 = load_index(storage_folder212)
    index213 = load_index(storage_folder213)
    index214 = load_index(storage_folder214)
    index215 = load_index(storage_folder215)
    index216 = load_index(storage_folder216)
    index217 = load_index(storage_folder217)
    index218 = load_index(storage_folder218)
    index219 = load_index(storage_folder219)
    index220 = load_index(storage_folder220)
    index221 = load_index(storage_folder221)
    index222 = load_index(storage_folder222)
    index223 = load_index(storage_folder223)
    index224 = load_index(storage_folder224)
    index225 = load_index(storage_folder225)
    index226 = load_index(storage_folder226)
    index227 = load_index(storage_folder227)
    index228 = load_index(storage_folder228)
    index229 = load_index(storage_folder229)
    index230 = load_index(storage_folder230)
    index231 = load_index(storage_folder231)
    index232 = load_index(storage_folder232)
    index233 = load_index(storage_folder233)
    index234 = load_index(storage_folder234)
    index235 = load_index(storage_folder235)
    index236 = load_index(storage_folder236)
    index237 = load_index(storage_folder237)
    index238 = load_index(storage_folder238)
    index239 = load_index(storage_folder239)
    index240 = load_index(storage_folder240)
    index241 = load_index(storage_folder241)
    index242 = load_index(storage_folder242)
    index243 = load_index(storage_folder243)
    index244 = load_index(storage_folder244)
    index245 = load_index(storage_folder245)
    index246 = load_index(storage_folder246)
    index247 = load_index(storage_folder247)
    index248 = load_index(storage_folder248)
    index249 = load_index(storage_folder249)
    index250 = load_index(storage_folder250)
    index251 = load_index(storage_folder251)
    index252 = load_index(storage_folder252)
    index253 = load_index(storage_folder253)
    index254 = load_index(storage_folder254)
    index255 = load_index(storage_folder255)
    index256 = load_index(storage_folder256)
    index257 = load_index(storage_folder257)
    index258 = load_index(storage_folder258)
    index259 = load_index(storage_folder259)
    index260 = load_index(storage_folder260)
    index261 = load_index(storage_folder261)
    index262 = load_index(storage_folder262)
    index263 = load_index(storage_folder263)
    index264 = load_index(storage_folder264)
    index265 = load_index(storage_folder265)
    index266 = load_index(storage_folder266)
    index267 = load_index(storage_folder267)
    index268 = load_index(storage_folder268)
    index269 = load_index(storage_folder269)
    index270 = load_index(storage_folder270)
    index271 = load_index(storage_folder271)
    index272 = load_index(storage_folder272)
    index273 = load_index(storage_folder273)
    index274 = load_index(storage_folder274)
    index275 = load_index(storage_folder275)
    index276 = load_index(storage_folder276)
    index277 = load_index(storage_folder277)
    index278 = load_index(storage_folder278)
    index279 = load_index(storage_folder279)
    index280 = load_index(storage_folder280)
    index281 = load_index(storage_folder281)
    index282 = load_index(storage_folder282)
    index283 = load_index(storage_folder283)
    index284 = load_index(storage_folder284)
    index285 = load_index(storage_folder285)
    index286 = load_index(storage_folder286)
    index287 = load_index(storage_folder287)
    index288 = load_index(storage_folder288)
    index289 = load_index(storage_folder289)
    index290 = load_index(storage_folder290)
    index291 = load_index(storage_folder291)
    index292 = load_index(storage_folder292)
    index293 = load_index(storage_folder293)
    index294 = load_index(storage_folder294)
    index295 = load_index(storage_folder295)
    index296 = load_index(storage_folder296)
    index297 = load_index(storage_folder297)
    index298 = load_index(storage_folder298)
    index299 = load_index(storage_folder299)
    index300 = load_index(storage_folder300)
    index301 = load_index(storage_folder301)
    index302 = load_index(storage_folder302)
    index303 = load_index(storage_folder303)
    index304 = load_index(storage_folder304)
    index305 = load_index(storage_folder305)
    index306 = load_index(storage_folder306)
    index307 = load_index(storage_folder307)
    index308 = load_index(storage_folder308)
    index309 = load_index(storage_folder309)
    index310 = load_index(storage_folder310)
    index311 = load_index(storage_folder311)
    index312 = load_index(storage_folder312)
    index313 = load_index(storage_folder313)
    index314 = load_index(storage_folder314)
    index315 = load_index(storage_folder315)
    index316 = load_index(storage_folder316)
    index317 = load_index(storage_folder317)
    index318 = load_index(storage_folder318)
    index319 = load_index(storage_folder319)
    index320 = load_index(storage_folder320)
    index321 = load_index(storage_folder321)
    index322 = load_index(storage_folder322)
    index323 = load_index(storage_folder323)
    index324 = load_index(storage_folder324)
    index325 = load_index(storage_folder325)
    index326 = load_index(storage_folder326)
    index327 = load_index(storage_folder327)
    index328 = load_index(storage_folder328)
    index329 = load_index(storage_folder329)
    index330 = load_index(storage_folder330)
    index331 = load_index(storage_folder331)
    index332 = load_index(storage_folder332)
    index333 = load_index(storage_folder333)
    index334 = load_index(storage_folder334)
    index335 = load_index(storage_folder335)
    index336 = load_index(storage_folder336)
    index337 = load_index(storage_folder337)
    index338 = load_index(storage_folder338)
    index339 = load_index(storage_folder339)
    index340 = load_index(storage_folder340)
    index341 = load_index(storage_folder341)
    index342 = load_index(storage_folder342)
    index343 = load_index(storage_folder343)
    index344 = load_index(storage_folder344)
    index345 = load_index(storage_folder345)
    index346 = load_index(storage_folder346)
    index347 = load_index(storage_folder347)
    index348 = load_index(storage_folder348)
    index349 = load_index(storage_folder349)
    index350 = load_index(storage_folder350)
    index351 = load_index(storage_folder351)
    index352 = load_index(storage_folder352)
    index353 = load_index(storage_folder353)
    index354 = load_index(storage_folder354)
    index355 = load_index(storage_folder355)
    index356 = load_index(storage_folder356)
    index357 = load_index(storage_folder357)
    index358 = load_index(storage_folder358)
    index359 = load_index(storage_folder359)
    index360 = load_index(storage_folder360)
    index361 = load_index(storage_folder361)
    index362 = load_index(storage_folder362)
    index363 = load_index(storage_folder363)
    index364 = load_index(storage_folder364)
    index365 = load_index(storage_folder365)
    index366 = load_index(storage_folder366)
    index367 = load_index(storage_folder367)
    index368 = load_index(storage_folder368)
    index369 = load_index(storage_folder369)
    index370 = load_index(storage_folder370)
    index371 = load_index(storage_folder371)
    index372 = load_index(storage_folder372)
    index373 = load_index(storage_folder373)
    index374 = load_index(storage_folder374)
    index375 = load_index(storage_folder375)
    index376 = load_index(storage_folder376)
    index377 = load_index(storage_folder377)
    index378 = load_index(storage_folder378)
    index379 = load_index(storage_folder379)
    index380 = load_index(storage_folder380)
    index381 = load_index(storage_folder381)
    index382 = load_index(storage_folder382)
    index383 = load_index(storage_folder383)
    index384 = load_index(storage_folder384)
    index385 = load_index(storage_folder385)
    index386 = load_index(storage_folder386)
    index387 = load_index(storage_folder387)
    index388 = load_index(storage_folder388)
    index389 = load_index(storage_folder389)
    index390 = load_index(storage_folder390)
    index391 = load_index(storage_folder391)
    index392 = load_index(storage_folder392)
    index393 = load_index(storage_folder393)
    index394 = load_index(storage_folder394)
    index395 = load_index(storage_folder395)
    index396 = load_index(storage_folder396)
    index397 = load_index(storage_folder397)
    index398 = load_index(storage_folder398)
    index399 = load_index(storage_folder399)
    index400 = load_index(storage_folder400)
    index401 = load_index(storage_folder401)
    index402 = load_index(storage_folder402)
    index403 = load_index(storage_folder403)
    index404 = load_index(storage_folder404)
    index405 = load_index(storage_folder405)
    index406 = load_index(storage_folder406)
    index407 = load_index(storage_folder407)
    index408 = load_index(storage_folder408)
    index409 = load_index(storage_folder409)
    index410 = load_index(storage_folder410)
    index411 = load_index(storage_folder411)
    index412 = load_index(storage_folder412)
    index413 = load_index(storage_folder413)
    index414 = load_index(storage_folder414)
    index415 = load_index(storage_folder415)
    index416 = load_index(storage_folder416)
    index417 = load_index(storage_folder417)
    index418 = load_index(storage_folder418)
    index419 = load_index(storage_folder419)
    index420 = load_index(storage_folder420)
    index421 = load_index(storage_folder421)
    index422 = load_index(storage_folder422)
    index423 = load_index(storage_folder423)
    index424 = load_index(storage_folder424)
    index425 = load_index(storage_folder425)
    index426 = load_index(storage_folder426)
    index427 = load_index(storage_folder427)
    index428 = load_index(storage_folder428)
    index429 = load_index(storage_folder429)
    index430 = load_index(storage_folder430)
    index431 = load_index(storage_folder431)
    index432 = load_index(storage_folder432)
    index433 = load_index(storage_folder433)
    index434 = load_index(storage_folder434)
    index435 = load_index(storage_folder435)
    index436 = load_index(storage_folder436)
    index437 = load_index(storage_folder437)
    index438 = load_index(storage_folder438)
    index439 = load_index(storage_folder439)
    index440 = load_index(storage_folder440)
    index441 = load_index(storage_folder441)
    index442 = load_index(storage_folder442)
    index443 = load_index(storage_folder443)
    index444 = load_index(storage_folder444)
    index445 = load_index(storage_folder445)
    index446 = load_index(storage_folder446)
    index447 = load_index(storage_folder447)
    index448 = load_index(storage_folder448)
    index449 = load_index(storage_folder449)
    index450 = load_index(storage_folder450)
    index451 = load_index(storage_folder451)
    index452 = load_index(storage_folder452)
    index453 = load_index(storage_folder453)
    index454 = load_index(storage_folder454)
    index455 = load_index(storage_folder455)
    index456 = load_index(storage_folder456)
    index457 = load_index(storage_folder457)
    index458 = load_index(storage_folder458)
    index459 = load_index(storage_folder459)
    index460 = load_index(storage_folder460)
    index461 = load_index(storage_folder461)
    index462 = load_index(storage_folder462)
    index463 = load_index(storage_folder463)
    index464 = load_index(storage_folder464)
    index465 = load_index(storage_folder465)
    index466 = load_index(storage_folder466)
    index467 = load_index(storage_folder467)
    index468 = load_index(storage_folder468)
    index469 = load_index(storage_folder469)
    index470 = load_index(storage_folder470)
    index471 = load_index(storage_folder471)
    index472 = load_index(storage_folder472)
    index473 = load_index(storage_folder473)
    index474 = load_index(storage_folder474)
    index475 = load_index(storage_folder475)
    index476 = load_index(storage_folder476)
    index477 = load_index(storage_folder477)
    index478 = load_index(storage_folder478)
    index479 = load_index(storage_folder479)
    index480 = load_index(storage_folder480)
    index481 = load_index(storage_folder481)
    index482 = load_index(storage_folder482)
    index483 = load_index(storage_folder483)
    index484 = load_index(storage_folder484)
    index485 = load_index(storage_folder485)
    index486 = load_index(storage_folder486)
    index487 = load_index(storage_folder487)
    index488 = load_index(storage_folder488)
    index489 = load_index(storage_folder489)
    index490 = load_index(storage_folder490)
    index491 = load_index(storage_folder491)
    index492 = load_index(storage_folder492)
    index493 = load_index(storage_folder493)
    index494 = load_index(storage_folder494)
    index495 = load_index(storage_folder495)
    index496 = load_index(storage_folder496)
    index497 = load_index(storage_folder497)
    index498 = load_index(storage_folder498)
    index499 = load_index(storage_folder499)
    index500 = load_index(storage_folder500)
    index501 = load_index(storage_folder501)
    index502 = load_index(storage_folder502)
    index503 = load_index(storage_folder503)
    index504 = load_index(storage_folder504)
    index505 = load_index(storage_folder505)
    index506 = load_index(storage_folder506)
    index507 = load_index(storage_folder507)
    index508 = load_index(storage_folder508)
    index509 = load_index(storage_folder509)
    index510 = load_index(storage_folder510)
    index511 = load_index(storage_folder511)
    index512 = load_index(storage_folder512)
    index513 = load_index(storage_folder513)
    index514 = load_index(storage_folder514)
    index515 = load_index(storage_folder515)
    index516 = load_index(storage_folder516)
    index517 = load_index(storage_folder517)
    index518 = load_index(storage_folder518)
    index519 = load_index(storage_folder519)
    index520 = load_index(storage_folder520)
    index521 = load_index(storage_folder521)
    index522 = load_index(storage_folder522)
    index523 = load_index(storage_folder523)
    index524 = load_index(storage_folder524)
    index525 = load_index(storage_folder525)
    index526 = load_index(storage_folder526)
    index527 = load_index(storage_folder527)
    index528 = load_index(storage_folder528)
    index529 = load_index(storage_folder529)
    index530 = load_index(storage_folder530)
    index531 = load_index(storage_folder531)
    index532 = load_index(storage_folder532)
    index533 = load_index(storage_folder533)
    index534 = load_index(storage_folder534)
    index535 = load_index(storage_folder535)
    index536 = load_index(storage_folder536)
    index537 = load_index(storage_folder537)
    index538 = load_index(storage_folder538)
    index539 = load_index(storage_folder539)
    index540 = load_index(storage_folder540)
    index541 = load_index(storage_folder541)
    index542 = load_index(storage_folder542)
    index543 = load_index(storage_folder543)
    index544 = load_index(storage_folder544)
    index545 = load_index(storage_folder545)
    index546 = load_index(storage_folder546)
    index547 = load_index(storage_folder547)
    index548 = load_index(storage_folder548)
    index549 = load_index(storage_folder549)
    index550 = load_index(storage_folder550)
    index551 = load_index(storage_folder551)
    index552 = load_index(storage_folder552)
    index553 = load_index(storage_folder553)
    index554 = load_index(storage_folder554)
    index555 = load_index(storage_folder555)
    index556 = load_index(storage_folder556)
    index557 = load_index(storage_folder557)
    index558 = load_index(storage_folder558)
    index559 = load_index(storage_folder559)
    index560 = load_index(storage_folder560)
    index561 = load_index(storage_folder561)
    index562 = load_index(storage_folder562)
    index563 = load_index(storage_folder563)
    index564 = load_index(storage_folder564)
    index565 = load_index(storage_folder565)
    index566 = load_index(storage_folder566)
    index567 = load_index(storage_folder567)
    index568 = load_index(storage_folder568)
    index569 = load_index(storage_folder569)
    index570 = load_index(storage_folder570)
    index571 = load_index(storage_folder571)
    index572 = load_index(storage_folder572)
    index573 = load_index(storage_folder573)
    index574 = load_index(storage_folder574)
    index575 = load_index(storage_folder575)
    index576 = load_index(storage_folder576)
    index577 = load_index(storage_folder577)
    index578 = load_index(storage_folder578)
    index579 = load_index(storage_folder579)
    index580 = load_index(storage_folder580)
    index581 = load_index(storage_folder581)
    index582 = load_index(storage_folder582)
    index583 = load_index(storage_folder583)
    index584 = load_index(storage_folder584)
    index585 = load_index(storage_folder585)
    index586 = load_index(storage_folder586)
    index587 = load_index(storage_folder587)
    index588 = load_index(storage_folder588)
    index589 = load_index(storage_folder589)
    index590 = load_index(storage_folder590)
    index591 = load_index(storage_folder591)
    index592 = load_index(storage_folder592)
    index593 = load_index(storage_folder593)
    index594 = load_index(storage_folder594)
    index595 = load_index(storage_folder595)
    index596 = load_index(storage_folder596)
    index597 = load_index(storage_folder597)
    index598 = load_index(storage_folder598)
    index599 = load_index(storage_folder599)
    index600 = load_index(storage_folder600)
    index601 = load_index(storage_folder601)
    index602 = load_index(storage_folder602)
    index603 = load_index(storage_folder603)
    index604 = load_index(storage_folder604)
    index605 = load_index(storage_folder605)
    index606 = load_index(storage_folder606)
    index607 = load_index(storage_folder607)
    index608 = load_index(storage_folder608)
    index609 = load_index(storage_folder609)
    index610 = load_index(storage_folder610)
    index611 = load_index(storage_folder611)
    index612 = load_index(storage_folder612)
    index613 = load_index(storage_folder613)
    index614 = load_index(storage_folder614)
    index615 = load_index(storage_folder615)
    index616 = load_index(storage_folder616)
    index617 = load_index(storage_folder617)
    index618 = load_index(storage_folder618)
    index619 = load_index(storage_folder619)
    index620 = load_index(storage_folder620)
    index621 = load_index(storage_folder621)
    index622 = load_index(storage_folder622)
    index623 = load_index(storage_folder623)
    index624 = load_index(storage_folder624)
    index625 = load_index(storage_folder625)
    index626 = load_index(storage_folder626)
    index627 = load_index(storage_folder627)
    index628 = load_index(storage_folder628)
    index629 = load_index(storage_folder629)
    index630 = load_index(storage_folder630)
    index631 = load_index(storage_folder631)
    index632 = load_index(storage_folder632)
    index633 = load_index(storage_folder633)
    index634 = load_index(storage_folder634)
    index635 = load_index(storage_folder635)
    index636 = load_index(storage_folder636)
    index637 = load_index(storage_folder637)
    index638 = load_index(storage_folder638)
    index639 = load_index(storage_folder639)
    index640 = load_index(storage_folder640)
    index641 = load_index(storage_folder641)
    index642 = load_index(storage_folder642)
    index643 = load_index(storage_folder643)
    index644 = load_index(storage_folder644)
    index645 = load_index(storage_folder645)
    index646 = load_index(storage_folder646)
    index647 = load_index(storage_folder647)
    index648 = load_index(storage_folder648)
    index649 = load_index(storage_folder649)
    index650 = load_index(storage_folder650)
    index651 = load_index(storage_folder651)
    index652 = load_index(storage_folder652)
    index653 = load_index(storage_folder653)
    index654 = load_index(storage_folder654)
    index655 = load_index(storage_folder655)
    index656 = load_index(storage_folder656)
    index657 = load_index(storage_folder657)
    index658 = load_index(storage_folder658)
    index659 = load_index(storage_folder659)
    index660 = load_index(storage_folder660)
    index661 = load_index(storage_folder661)
    index662 = load_index(storage_folder662)
    index663 = load_index(storage_folder663)
    index664 = load_index(storage_folder664)
    index665 = load_index(storage_folder665)
    index666 = load_index(storage_folder666)
    index667 = load_index(storage_folder667)
    index668 = load_index(storage_folder668)
    index669 = load_index(storage_folder669)
    index670 = load_index(storage_folder670)
    index671 = load_index(storage_folder671)
    index672 = load_index(storage_folder672)
    index673 = load_index(storage_folder673)
    index674 = load_index(storage_folder674)
    index675 = load_index(storage_folder675)
    index676 = load_index(storage_folder676)
    index677 = load_index(storage_folder677)
    index678 = load_index(storage_folder678)
    index679 = load_index(storage_folder679)
    index680 = load_index(storage_folder680)
    index681 = load_index(storage_folder681)
    index682 = load_index(storage_folder682)
    index683 = load_index(storage_folder683)
    index684 = load_index(storage_folder684)
    index685 = load_index(storage_folder685)
    index686 = load_index(storage_folder686)
    index687 = load_index(storage_folder687)
    index688 = load_index(storage_folder688)
    index689 = load_index(storage_folder689)
    index690 = load_index(storage_folder690)
    index691 = load_index(storage_folder691)
    index692 = load_index(storage_folder692)
    index693 = load_index(storage_folder693)
    index694 = load_index(storage_folder694)
    index695 = load_index(storage_folder695)
    index696 = load_index(storage_folder696)
    index697 = load_index(storage_folder697)
    index698 = load_index(storage_folder698)
    index699 = load_index(storage_folder699)
    index700 = load_index(storage_folder700)
    index701 = load_index(storage_folder701)
    index702 = load_index(storage_folder702)
    index703 = load_index(storage_folder703)
    index704 = load_index(storage_folder704)
    index705 = load_index(storage_folder705)
    index706 = load_index(storage_folder706)
    index707 = load_index(storage_folder707)
    index708 = load_index(storage_folder708)
    index709 = load_index(storage_folder709)
    index710 = load_index(storage_folder710)
    index711 = load_index(storage_folder711)
    index712 = load_index(storage_folder712)
    index713 = load_index(storage_folder713)
    index714 = load_index(storage_folder714)
    index715 = load_index(storage_folder715)
    index716 = load_index(storage_folder716)
    index717 = load_index(storage_folder717)
    index718 = load_index(storage_folder718)
    index719 = load_index(storage_folder719)
    index720 = load_index(storage_folder720)
    index721 = load_index(storage_folder721)
    index722 = load_index(storage_folder722)
    index723 = load_index(storage_folder723)
    index724 = load_index(storage_folder724)
    index725 = load_index(storage_folder725)
    index726 = load_index(storage_folder726)
    index727 = load_index(storage_folder727)
    index728 = load_index(storage_folder728)
    index729 = load_index(storage_folder729)
    index730 = load_index(storage_folder730)
    index731 = load_index(storage_folder731)
    index732 = load_index(storage_folder732)
    index733 = load_index(storage_folder733)
    index734 = load_index(storage_folder734)
    index735 = load_index(storage_folder735)
    index736 = load_index(storage_folder736)
    index737 = load_index(storage_folder737)
    index738 = load_index(storage_folder738)
    index739 = load_index(storage_folder739)
    index740 = load_index(storage_folder740)
    index741 = load_index(storage_folder741)
    index742 = load_index(storage_folder742)
    index743 = load_index(storage_folder743)
    index744 = load_index(storage_folder744)
    index745 = load_index(storage_folder745)
    index746 = load_index(storage_folder746)
    index747 = load_index(storage_folder747)
    index748 = load_index(storage_folder748)
    index749 = load_index(storage_folder749)
    index750 = load_index(storage_folder750)
    index751 = load_index(storage_folder751)
    index752 = load_index(storage_folder752)
    index753 = load_index(storage_folder753)
    index754 = load_index(storage_folder754)
    index755 = load_index(storage_folder755)
    index756 = load_index(storage_folder756)
    index757 = load_index(storage_folder757)
    index758 = load_index(storage_folder758)
    index759 = load_index(storage_folder759)
    index760 = load_index(storage_folder760)
    index761 = load_index(storage_folder761)
    index762 = load_index(storage_folder762)
    index763 = load_index(storage_folder763)
    index764 = load_index(storage_folder764)
    index765 = load_index(storage_folder765)
    index766 = load_index(storage_folder766)
    index767 = load_index(storage_folder767)
    index768 = load_index(storage_folder768)
    index769 = load_index(storage_folder769)
    index770 = load_index(storage_folder770)
    index771 = load_index(storage_folder771)
    index772 = load_index(storage_folder772)
    index773 = load_index(storage_folder773)
    index774 = load_index(storage_folder774)
    index775 = load_index(storage_folder775)
    index776 = load_index(storage_folder776)
    index777 = load_index(storage_folder777)
    index778 = load_index(storage_folder778)

    graph = ComposableGraph.from_indices(
        ListIndex,
        [index1,
        index2,
        index3,
        index4,
        index5,
        index6,
        index7,
        index8,
        index9,
        index10,
        index11,
        index12,
        index13,
        index14,
        index15,
        index16,
        index17,
        index18,
        index19,
        index20,
        index21,
        index22,
        index23,
        index24,
        index25,
        index26,
        index27,
        index28,
        index29,
        index30,
        index31,
        index32,
        index33,
        index34,
        index35,
        index36,
        index37,
        index38,
        index39,
        index40,
        index41,
        index42,
        index43,
        index44,
        index45,
        index46,
        index47,
        index48,
        index49,
        index50,
        index51,
        index52,
        index53,
        index54,
        index55,
        index56,
        index57,
        index58,
        index59,
        index60,
        index61,
        index62,
        index63,
        index64,
        index65,
        index66,
        index67,
        index68,
        index69,
        index70,
        index71,
        index72,
        index73,
        index74,
        index75,
        index76,
        index77,
        index78,
        index79,
        index80,
        index81,
        index82,
        index83,
        index84,
        index85,
        index86,
        index87,
        index88,
        index89,
        index90,
        index91,
        index92,
        index93,
        index94,
        index95,
        index96,
        index97,
        index98,
        index99,
        index100,
        index101,
        index102,
        index103,
        index104,
        index105,
        index106,
        index107,
        index108,
        index109,
        index110,
        index111,
        index112,
        index113,
        index114,
        index115,
        index116,
        index117,
        index118,
        index119,
        index120,
        index121,
        index122,
        index123,
        index124,
        index125,
        index126,
        index127,
        index128,
        index129,
        index130,
        index131,
        index132,
        index133,
        index134,
        index135,
        index136,
        index137,
        index138,
        index139,
        index140,
        index141,
        index142,
        index143,
        index144,
        index145,
        index146,
        index147,
        index148,
        index149,
        index150,
        index151,
        index152,
        index153,
        index154,
        index155,
        index156,
        index157,
        index158,
        index159,
        index160,
        index161,
        index162,
        index163,
        index164,
        index165,
        index166,
        index167,
        index168,
        index169,
        index170,
        index171,
        index172,
        index173,
        index174,
        index175,
        index176,
        index177,
        index178,
        index179,
        index180,
        index181,
        index182,
        index183,
        index184,
        index185,
        index186,
        index187,
        index188,
        index189,
        index190,
        index191,
        index192,
        index193,
        index194,
        index195,
        index196,
        index197,
        index198,
        index199,
        index200,
        index201,
        index202,
        index203,
        index204,
        index205,
        index206,
        index207,
        index208,
        index209,
        index210,
        index211,
        index212,
        index213,
        index214,
        index215,
        index216,
        index217,
        index218,
        index219,
        index220,
        index221,
        index222,
        index223,
        index224,
        index225,
        index226,
        index227,
        index228,
        index229,
        index230,
        index231,
        index232,
        index233,
        index234,
        index235,
        index236,
        index237,
        index238,
        index239,
        index240,
        index241,
        index242,
        index243,
        index244,
        index245,
        index246,
        index247,
        index248,
        index249,
        index250,
        index251,
        index252,
        index253,
        index254,
        index255,
        index256,
        index257,
        index258,
        index259,
        index260,
        index261,
        index262,
        index263,
        index264,
        index265,
        index266,
        index267,
        index268,
        index269,
        index270,
        index271,
        index272,
        index273,
        index274,
        index275,
        index276,
        index277,
        index278,
        index279,
        index280,
        index281,
        index282,
        index283,
        index284,
        index285,
        index286,
        index287,
        index288,
        index289,
        index290,
        index291,
        index292,
        index293,
        index294,
        index295,
        index296,
        index297,
        index298,
        index299,
        index300,
        index301,
        index302,
        index303,
        index304,
        index305,
        index306,
        index307,
        index308,
        index309,
        index310,
        index311,
        index312,
        index313,
        index314,
        index315,
        index316,
        index317,
        index318,
        index319,
        index320,
        index321,
        index322,
        index323,
        index324,
        index325,
        index326,
        index327,
        index328,
        index329,
        index330,
        index331,
        index332,
        index333,
        index334,
        index335,
        index336,
        index337,
        index338,
        index339,
        index340,
        index341,
        index342,
        index343,
        index344,
        index345,
        index346,
        index347,
        index348,
        index349,
        index350,
        index351,
        index352,
        index353,
        index354,
        index355,
        index356,
        index357,
        index358,
        index359,
        index360,
        index361,
        index362,
        index363,
        index364,
        index365,
        index366,
        index367,
        index368,
        index369,
        index370,
        index371,
        index372,
        index373,
        index374,
        index375,
        index376,
        index377,
        index378,
        index379,
        index380,
        index381,
        index382,
        index383,
        index384,
        index385,
        index386,
        index387,
        index388,
        index389,
        index390,
        index391,
        index392,
        index393,
        index394,
        index395,
        index396,
        index397,
        index398,
        index399,
        index400,
        index401,
        index402,
        index403,
        index404,
        index405,
        index406,
        index407,
        index408,
        index409,
        index410,
        index411,
        index412,
        index413,
        index414,
        index415,
        index416,
        index417,
        index418,
        index419,
        index420,
        index421,
        index422,
        index423,
        index424,
        index425,
        index426,
        index427,
        index428,
        index429,
        index430,
        index431,
        index432,
        index433,
        index434,
        index435,
        index436,
        index437,
        index438,
        index439,
        index440,
        index441,
        index442,
        index443,
        index444,
        index445,
        index446,
        index447,
        index448,
        index449,
        index450,
        index451,
        index452,
        index453,
        index454,
        index455,
        index456,
        index457,
        index458,
        index459,
        index460,
        index461,
        index462,
        index463,
        index464,
        index465,
        index466,
        index467,
        index468,
        index469,
        index470,
        index471,
        index472,
        index473,
        index474,
        index475,
        index476,
        index477,
        index478,
        index479,
        index480,
        index481,
        index482,
        index483,
        index484,
        index485,
        index486,
        index487,
        index488,
        index489,
        index490,
        index491,
        index492,
        index493,
        index494,
        index495,
        index496,
        index497,
        index498,
        index499,
        index500,
        index501,
        index502,
        index503,
        index504,
        index505,
        index506,
        index507,
        index508,
        index509,
        index510,
        index511,
        index512,
        index513,
        index514,
        index515,
        index516,
        index517,
        index518,
        index519,
        index520,
        index521,
        index522,
        index523,
        index524,
        index525,
        index526,
        index527,
        index528,
        index529,
        index530,
        index531,
        index532,
        index533,
        index534,
        index535,
        index536,
        index537,
        index538,
        index539,
        index540,
        index541,
        index542,
        index543,
        index544,
        index545,
        index546,
        index547,
        index548,
        index549,
        index550,
        index551,
        index552,
        index553,
        index554,
        index555,
        index556,
        index557,
        index558,
        index559,
        index560,
        index561,
        index562,
        index563,
        index564,
        index565,
        index566,
        index567,
        index568,
        index569,
        index570,
        index571,
        index572,
        index573,
        index574,
        index575,
        index576,
        index577,
        index578,
        index579,
        index580,
        index581,
        index582,
        index583,
        index584,
        index585,
        index586,
        index587,
        index588,
        index589,
        index590,
        index591,
        index592,
        index593,
        index594,
        index595,
        index596,
        index597,
        index598,
        index599,
        index600,
        index601,
        index602,
        index603,
        index604,
        index605,
        index606,
        index607,
        index608,
        index609,
        index610,
        index611,
        index612,
        index613,
        index614,
        index615,
        index616,
        index617,
        index618,
        index619,
        index620,
        index621,
        index622,
        index623,
        index624,
        index625,
        index626,
        index627,
        index628,
        index629,
        index630,
        index631,
        index632,
        index633,
        index634,
        index635,
        index636,
        index637,
        index638,
        index639,
        index640,
        index641,
        index642,
        index643,
        index644,
        index645,
        index646,
        index647,
        index648,
        index649,
        index650,
        index651,
        index652,
        index653,
        index654,
        index655,
        index656,
        index657,
        index658,
        index659,
        index660,
        index661,
        index662,
        index663,
        index664,
        index665,
        index666,
        index667,
        index668,
        index669,
        index670,
        index671,
        index672,
        index673,
        index674,
        index675,
        index676,
        index677,
        index678,
        index679,
        index680,
        index681,
        index682,
        index683,
        index684,
        index685,
        index686,
        index687,
        index688,
        index689,
        index690,
        index691,
        index692,
        index693,
        index694,
        index695,
        index696,
        index697,
        index698,
        index699,
        index700,
        index701,
        index702,
        index703,
        index704,
        index705,
        index706,
        index707,
        index708,
        index709,
        index710,
        index711,
        index712,
        index713,
        index714,
        index715,
        index716,
        index717,
        index718,
        index719,
        index720,
        index721,
        index722,
        index723,
        index724,
        index725,
        index726,
        index727,
        index728,
        index729,
        index730,
        index731,
        index732,
        index733,
        index734,
        index735,
        index736,
        index737,
        index738,
        index739,
        index740,
        index741,
        index742,
        index743,
        index744,
        index745,
        index746,
        index747,
        index748,
        index749,
        index750,
        index751,
        index752,
        index753,
        index754,
        index755,
        index756,
        index757,
        index758,
        index759,
        index760,
        index761,
        index762,
        index763,
        index764,
        index765,
        index766,
        index767,
        index768,
        index769,
        index770,
        index771,
        index772,
        index773,
        index774,
        index775,
        index776,
        index777,
        index778,
        ],
        index_summaries=["chunk1",
                        "chunk2",
                        "chunk3",
                        "chunk4",
                        "chunk5",
                        "chunk6",
                        "chunk7",
                        "chunk8",
                        "chunk9",
                        "chunk10",
                        "chunk11",
                        "chunk12",
                        "chunk13",
                        "chunk14",
                        "chunk15",
                        "chunk16",
                        "chunk17",
                        "chunk18",
                        "chunk19",
                        "chunk20",
                        "chunk21",
                        "chunk22",
                        "chunk23",
                        "chunk24",
                        "chunk25",
                        "chunk26",
                        "chunk27",
                        "chunk28",
                        "chunk29",
                        "chunk30",
                        "chunk31",
                        "chunk32",
                        "chunk33",
                        "chunk34",
                        "chunk35",
                        "chunk36",
                        "chunk37",
                        "chunk38",
                        "chunk39",
                        "chunk40",
                        "chunk41",
                        "chunk42",
                        "chunk43",
                        "chunk44",
                        "chunk45",
                        "chunk46",
                        "chunk47",
                        "chunk48",
                        "chunk49",
                        "chunk50",
                        "chunk51",
                        "chunk52",
                        "chunk53",
                        "chunk54",
                        "chunk55",
                        "chunk56",
                        "chunk57",
                        "chunk58",
                        "chunk59",
                        "chunk60",
                        "chunk61",
                        "chunk62",
                        "chunk63",
                        "chunk64",
                        "chunk65",
                        "chunk66",
                        "chunk67",
                        "chunk68",
                        "chunk69",
                        "chunk70",
                        "chunk71",
                        "chunk72",
                        "chunk73",
                        "chunk74",
                        "chunk75",
                        "chunk76",
                        "chunk77",
                        "chunk78",
                        "chunk79",
                        "chunk80",
                        "chunk81",
                        "chunk82",
                        "chunk83",
                        "chunk84",
                        "chunk85",
                        "chunk86",
                        "chunk87",
                        "chunk88",
                        "chunk89",
                        "chunk90",
                        "chunk91",
                        "chunk92",
                        "chunk93",
                        "chunk94",
                        "chunk95",
                        "chunk96",
                        "chunk97",
                        "chunk98",
                        "chunk99",
                        "chunk100",
                        "chunk101",
                        "chunk102",
                        "chunk103",
                        "chunk104",
                        "chunk105",
                        "chunk106",
                        "chunk107",
                        "chunk108",
                        "chunk109",
                        "chunk110",
                        "chunk111",
                        "chunk112",
                        "chunk113",
                        "chunk114",
                        "chunk115",
                        "chunk116",
                        "chunk117",
                        "chunk118",
                        "chunk119",
                        "chunk120",
                        "chunk121",
                        "chunk122",
                        "chunk123",
                        "chunk124",
                        "chunk125",
                        "chunk126",
                        "chunk127",
                        "chunk128",
                        "chunk129",
                        "chunk130",
                        "chunk131",
                        "chunk132",
                        "chunk133",
                        "chunk134",
                        "chunk135",
                        "chunk136",
                        "chunk137",
                        "chunk138",
                        "chunk139",
                        "chunk140",
                        "chunk141",
                        "chunk142",
                        "chunk143",
                        "chunk144",
                        "chunk145",
                        "chunk146",
                        "chunk147",
                        "chunk148",
                        "chunk149",
                        "chunk150",
                        "chunk151",
                        "chunk152",
                        "chunk153",
                        "chunk154",
                        "chunk155",
                        "chunk156",
                        "chunk157",
                        "chunk158",
                        "chunk159",
                        "chunk160",
                        "chunk161",
                        "chunk162",
                        "chunk163",
                        "chunk164",
                        "chunk165",
                        "chunk166",
                        "chunk167",
                        "chunk168",
                        "chunk169",
                        "chunk170",
                        "chunk171",
                        "chunk172",
                        "chunk173",
                        "chunk174",
                        "chunk175",
                        "chunk176",
                        "chunk177",
                        "chunk178",
                        "chunk179",
                        "chunk180",
                        "chunk181",
                        "chunk182",
                        "chunk183",
                        "chunk184",
                        "chunk185",
                        "chunk186",
                        "chunk187",
                        "chunk188",
                        "chunk189",
                        "chunk190",
                        "chunk191",
                        "chunk192",
                        "chunk193",
                        "chunk194",
                        "chunk195",
                        "chunk196",
                        "chunk197",
                        "chunk198",
                        "chunk199",
                        "chunk200",
                        "chunk201",
                        "chunk202",
                        "chunk203",
                        "chunk204",
                        "chunk205",
                        "chunk206",
                        "chunk207",
                        "chunk208",
                        "chunk209",
                        "chunk210",
                        "chunk211",
                        "chunk212",
                        "chunk213",
                        "chunk214",
                        "chunk215",
                        "chunk216",
                        "chunk217",
                        "chunk218",
                        "chunk219",
                        "chunk220",
                        "chunk221",
                        "chunk222",
                        "chunk223",
                        "chunk224",
                        "chunk225",
                        "chunk226",
                        "chunk227",
                        "chunk228",
                        "chunk229",
                        "chunk230",
                        "chunk231",
                        "chunk232",
                        "chunk233",
                        "chunk234",
                        "chunk235",
                        "chunk236",
                        "chunk237",
                        "chunk238",
                        "chunk239",
                        "chunk240",
                        "chunk241",
                        "chunk242",
                        "chunk243",
                        "chunk244",
                        "chunk245",
                        "chunk246",
                        "chunk247",
                        "chunk248",
                        "chunk249",
                        "chunk250",
                        "chunk251",
                        "chunk252",
                        "chunk253",
                        "chunk254",
                        "chunk255",
                        "chunk256",
                        "chunk257",
                        "chunk258",
                        "chunk259",
                        "chunk260",
                        "chunk261",
                        "chunk262",
                        "chunk263",
                        "chunk264",
                        "chunk265",
                        "chunk266",
                        "chunk267",
                        "chunk268",
                        "chunk269",
                        "chunk270",
                        "chunk271",
                        "chunk272",
                        "chunk273",
                        "chunk274",
                        "chunk275",
                        "chunk276",
                        "chunk277",
                        "chunk278",
                        "chunk279",
                        "chunk280",
                        "chunk281",
                        "chunk282",
                        "chunk283",
                        "chunk284",
                        "chunk285",
                        "chunk286",
                        "chunk287",
                        "chunk288",
                        "chunk289",
                        "chunk290",
                        "chunk291",
                        "chunk292",
                        "chunk293",
                        "chunk294",
                        "chunk295",
                        "chunk296",
                        "chunk297",
                        "chunk298",
                        "chunk299",
                        "chunk300",
                        "chunk301",
                        "chunk302",
                        "chunk303",
                        "chunk304",
                        "chunk305",
                        "chunk306",
                        "chunk307",
                        "chunk308",
                        "chunk309",
                        "chunk310",
                        "chunk311",
                        "chunk312",
                        "chunk313",
                        "chunk314",
                        "chunk315",
                        "chunk316",
                        "chunk317",
                        "chunk318",
                        "chunk319",
                        "chunk320",
                        "chunk321",
                        "chunk322",
                        "chunk323",
                        "chunk324",
                        "chunk325",
                        "chunk326",
                        "chunk327",
                        "chunk328",
                        "chunk329",
                        "chunk330",
                        "chunk331",
                        "chunk332",
                        "chunk333",
                        "chunk334",
                        "chunk335",
                        "chunk336",
                        "chunk337",
                        "chunk338",
                        "chunk339",
                        "chunk340",
                        "chunk341",
                        "chunk342",
                        "chunk343",
                        "chunk344",
                        "chunk345",
                        "chunk346",
                        "chunk347",
                        "chunk348",
                        "chunk349",
                        "chunk350",
                        "chunk351",
                        "chunk352",
                        "chunk353",
                        "chunk354",
                        "chunk355",
                        "chunk356",
                        "chunk357",
                        "chunk358",
                        "chunk359",
                        "chunk360",
                        "chunk361",
                        "chunk362",
                        "chunk363",
                        "chunk364",
                        "chunk365",
                        "chunk366",
                        "chunk367",
                        "chunk368",
                        "chunk369",
                        "chunk370",
                        "chunk371",
                        "chunk372",
                        "chunk373",
                        "chunk374",
                        "chunk375",
                        "chunk376",
                        "chunk377",
                        "chunk378",
                        "chunk379",
                        "chunk380",
                        "chunk381",
                        "chunk382",
                        "chunk383",
                        "chunk384",
                        "chunk385",
                        "chunk386",
                        "chunk387",
                        "chunk388",
                        "chunk389",
                        "chunk390",
                        "chunk391",
                        "chunk392",
                        "chunk393",
                        "chunk394",
                        "chunk395",
                        "chunk396",
                        "chunk397",
                        "chunk398",
                        "chunk399",
                        "chunk400",
                        "chunk401",
                        "chunk402",
                        "chunk403",
                        "chunk404",
                        "chunk405",
                        "chunk406",
                        "chunk407",
                        "chunk408",
                        "chunk409",
                        "chunk410",
                        "chunk411",
                        "chunk412",
                        "chunk413",
                        "chunk414",
                        "chunk415",
                        "chunk416",
                        "chunk417",
                        "chunk418",
                        "chunk419",
                        "chunk420",
                        "chunk421",
                        "chunk422",
                        "chunk423",
                        "chunk424",
                        "chunk425",
                        "chunk426",
                        "chunk427",
                        "chunk428",
                        "chunk429",
                        "chunk430",
                        "chunk431",
                        "chunk432",
                        "chunk433",
                        "chunk434",
                        "chunk435",
                        "chunk436",
                        "chunk437",
                        "chunk438",
                        "chunk439",
                        "chunk440",
                        "chunk441",
                        "chunk442",
                        "chunk443",
                        "chunk444",
                        "chunk445",
                        "chunk446",
                        "chunk447",
                        "chunk448",
                        "chunk449",
                        "chunk450",
                        "chunk451",
                        "chunk452",
                        "chunk453",
                        "chunk454",
                        "chunk455",
                        "chunk456",
                        "chunk457",
                        "chunk458",
                        "chunk459",
                        "chunk460",
                        "chunk461",
                        "chunk462",
                        "chunk463",
                        "chunk464",
                        "chunk465",
                        "chunk466",
                        "chunk467",
                        "chunk468",
                        "chunk469",
                        "chunk470",
                        "chunk471",
                        "chunk472",
                        "chunk473",
                        "chunk474",
                        "chunk475",
                        "chunk476",
                        "chunk477",
                        "chunk478",
                        "chunk479",
                        "chunk480",
                        "chunk481",
                        "chunk482",
                        "chunk483",
                        "chunk484",
                        "chunk485",
                        "chunk486",
                        "chunk487",
                        "chunk488",
                        "chunk489",
                        "chunk490",
                        "chunk491",
                        "chunk492",
                        "chunk493",
                        "chunk494",
                        "chunk495",
                        "chunk496",
                        "chunk497",
                        "chunk498",
                        "chunk499",
                        "chunk500",
                        "chunk501",
                        "chunk502",
                        "chunk503",
                        "chunk504",
                        "chunk505",
                        "chunk506",
                        "chunk507",
                        "chunk508",
                        "chunk509",
                        "chunk510",
                        "chunk511",
                        "chunk512",
                        "chunk513",
                        "chunk514",
                        "chunk515",
                        "chunk516",
                        "chunk517",
                        "chunk518",
                        "chunk519",
                        "chunk520",
                        "chunk521",
                        "chunk522",
                        "chunk523",
                        "chunk524",
                        "chunk525",
                        "chunk526",
                        "chunk527",
                        "chunk528",
                        "chunk529",
                        "chunk530",
                        "chunk531",
                        "chunk532",
                        "chunk533",
                        "chunk534",
                        "chunk535",
                        "chunk536",
                        "chunk537",
                        "chunk538",
                        "chunk539",
                        "chunk540",
                        "chunk541",
                        "chunk542",
                        "chunk543",
                        "chunk544",
                        "chunk545",
                        "chunk546",
                        "chunk547",
                        "chunk548",
                        "chunk549",
                        "chunk550",
                        "chunk551",
                        "chunk552",
                        "chunk553",
                        "chunk554",
                        "chunk555",
                        "chunk556",
                        "chunk557",
                        "chunk558",
                        "chunk559",
                        "chunk560",
                        "chunk561",
                        "chunk562",
                        "chunk563",
                        "chunk564",
                        "chunk565",
                        "chunk566",
                        "chunk567",
                        "chunk568",
                        "chunk569",
                        "chunk570",
                        "chunk571",
                        "chunk572",
                        "chunk573",
                        "chunk574",
                        "chunk575",
                        "chunk576",
                        "chunk577",
                        "chunk578",
                        "chunk579",
                        "chunk580",
                        "chunk581",
                        "chunk582",
                        "chunk583",
                        "chunk584",
                        "chunk585",
                        "chunk586",
                        "chunk587",
                        "chunk588",
                        "chunk589",
                        "chunk590",
                        "chunk591",
                        "chunk592",
                        "chunk593",
                        "chunk594",
                        "chunk595",
                        "chunk596",
                        "chunk597",
                        "chunk598",
                        "chunk599",
                        "chunk600",
                        "chunk601",
                        "chunk602",
                        "chunk603",
                        "chunk604",
                        "chunk605",
                        "chunk606",
                        "chunk607",
                        "chunk608",
                        "chunk609",
                        "chunk610",
                        "chunk611",
                        "chunk612",
                        "chunk613",
                        "chunk614",
                        "chunk615",
                        "chunk616",
                        "chunk617",
                        "chunk618",
                        "chunk619",
                        "chunk620",
                        "chunk621",
                        "chunk622",
                        "chunk623",
                        "chunk624",
                        "chunk625",
                        "chunk626",
                        "chunk627",
                        "chunk628",
                        "chunk629",
                        "chunk630",
                        "chunk631",
                        "chunk632",
                        "chunk633",
                        "chunk634",
                        "chunk635",
                        "chunk636",
                        "chunk637",
                        "chunk638",
                        "chunk639",
                        "chunk640",
                        "chunk641",
                        "chunk642",
                        "chunk643",
                        "chunk644",
                        "chunk645",
                        "chunk646",
                        "chunk647",
                        "chunk648",
                        "chunk649",
                        "chunk650",
                        "chunk651",
                        "chunk652",
                        "chunk653",
                        "chunk654",
                        "chunk655",
                        "chunk656",
                        "chunk657",
                        "chunk658",
                        "chunk659",
                        "chunk660",
                        "chunk661",
                        "chunk662",
                        "chunk663",
                        "chunk664",
                        "chunk665",
                        "chunk666",
                        "chunk667",
                        "chunk668",
                        "chunk669",
                        "chunk670",
                        "chunk671",
                        "chunk672",
                        "chunk673",
                        "chunk674",
                        "chunk675",
                        "chunk676",
                        "chunk677",
                        "chunk678",
                        "chunk679",
                        "chunk680",
                        "chunk681",
                        "chunk682",
                        "chunk683",
                        "chunk684",
                        "chunk685",
                        "chunk686",
                        "chunk687",
                        "chunk688",
                        "chunk689",
                        "chunk690",
                        "chunk691",
                        "chunk692",
                        "chunk693",
                        "chunk694",
                        "chunk695",
                        "chunk696",
                        "chunk697",
                        "chunk698",
                        "chunk699",
                        "chunk700",
                        "chunk701",
                        "chunk702",
                        "chunk703",
                        "chunk704",
                        "chunk705",
                        "chunk706",
                        "chunk707",
                        "chunk708",
                        "chunk709",
                        "chunk710",
                        "chunk711",
                        "chunk712",
                        "chunk713",
                        "chunk714",
                        "chunk715",
                        "chunk716",
                        "chunk717",
                        "chunk718",
                        "chunk719",
                        "chunk720",
                        "chunk721",
                        "chunk722",
                        "chunk723",
                        "chunk724",
                        "chunk725",
                        "chunk726",
                        "chunk727",
                        "chunk728",
                        "chunk729",
                        "chunk730",
                        "chunk731",
                        "chunk732",
                        "chunk733",
                        "chunk734",
                        "chunk735",
                        "chunk736",
                        "chunk737",
                        "chunk738",
                        "chunk739",
                        "chunk740",
                        "chunk741",
                        "chunk742",
                        "chunk743",
                        "chunk744",
                        "chunk745",
                        "chunk746",
                        "chunk747",
                        "chunk748",
                        "chunk749",
                        "chunk750",
                        "chunk751",
                        "chunk752",
                        "chunk753",
                        "chunk754",
                        "chunk755",
                        "chunk756",
                        "chunk757",
                        "chunk758",
                        "chunk759",
                        "chunk760",
                        "chunk761",
                        "chunk762",
                        "chunk763",
                        "chunk764",
                        "chunk765",
                        "chunk766",
                        "chunk767",
                        "chunk768",
                        "chunk769",
                        "chunk770",
                        "chunk771",
                        "chunk772",
                        "chunk773",
                        "chunk774",
                        "chunk775",
                        "chunk776",
                        "chunk777",
                        "chunk778"],
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


if __name__ == "__main__":
    import os
    import config_file as cf

    os.environ['OPENAI_API_KEY'] = cf.OAI_KEY

    INDEX_DIRECTORY = cf.STORAGE_FOLDER

    if not INDEX_DIRECTORY:
        INDEX_DIRECTORY = "./storage"

    create_index(INDEX_DIRECTORY)
