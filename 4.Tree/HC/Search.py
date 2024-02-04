from typing import Dict

search_cadidates = ["as", "ase", "asc", "asde", "ascff", "asced","b","bf"]
search_dict: Dict[str, dict | str | None] = {}


def dict_builder(tree_as_dic: dict, char_set: str, i: int, char_set_len: int) -> None: 
    # base case
    if i > char_set_len - 1:
        return
    assert isinstance(tree_as_dic, dict)
    cur_char = char_set[i]
    try:
        cur_dict = tree_as_dic[cur_char]
    except KeyError:
        cur_dict: Dict[str, dict] = {} 
        tree_as_dic[cur_char] = cur_dict
    dict_builder(cur_dict, char_set, i + 1, char_set_len)

for cur_char in search_cadidates: #O(nk) where n is len(words) k = char in word
    cur_len = len(cur_char)
    dict_builder(search_dict,cur_char,0,cur_len)

print(search_dict)

def dict_finder(cur_dict,cur_key,agg_char="",agg=[]):
    """
    tail recursion
    """
    if len(cur_dict) == 0:
        agg.append(agg_char)
        return
    agg_char += cur_key
    for next_dict in cur_dict:
        print(next_dict)
    return agg


test = dict_finder(search_dict,"a")
print(test)

