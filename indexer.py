import os
from collections import defaultdict
from preprocess import preprocess

def load_documents(folder_path):
    documents = {}
    for idx, filename in enumerate(sorted(os.listdir(folder_path))):
        with open(os.path.join(folder_path, filename), encoding='utf-8') as f:
            documents[idx] = f.read()
    return documents


def build_dictionary(documents):
    dictionary = defaultdict(int)

    for doc_id, text in documents.items():
        tokens = set(preprocess(text))
        for term in tokens:
            dictionary[term] += 1

    return dictionary


def build_inverted_index(documents):
    inverted_index = defaultdict(list)

    for doc_id, text in documents.items():
        tokens = set(preprocess(text))
        for term in tokens:
            inverted_index[term].append(doc_id)

    return inverted_index
