# src/indexing.py
from collections import defaultdict
from typing import Dict, List, Tuple

def build_dictionary(documents: Dict[int, List[str]]) -> Dict[str, int]:
    """ساخت دیکشنری: واژه → تعداد اسناد شامل آن"""
    dictionary = defaultdict(int)
    for tokens in documents.values():
        for term in set(tokens):  # set برای جلوگیری از تکرار در یک سند
            dictionary[term] += 1
    return dict(dictionary)

def build_inverted_index(documents: Dict[int, List[str]]) -> Dict[str, List[int]]:
    """ساخت نمایه معکوس: واژه → [docID1, docID2, ...]"""
    inverted_index = defaultdict(list)
    for doc_id, tokens in documents.items():
        for term in set(tokens):
            inverted_index[term].append(doc_id)  # should be int
    return dict(inverted_index)