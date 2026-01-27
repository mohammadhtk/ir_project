import math
from collections import defaultdict
from preprocess import preprocess

def compute_tf(tokens):
    tf = defaultdict(int)
    for token in tokens:
        tf[token] += 1
    return tf


def compute_all_tf(documents):
    docs_tf = {}
    for doc_id, text in documents.items():
        tokens = preprocess(text)
        docs_tf[doc_id] = compute_tf(tokens)
    return docs_tf


def compute_idf(dictionary, N):
    idf = {}
    for term, df in dictionary.items():
        idf[term] = math.log(N / df)
    return idf


def compute_tfidf(tf, idf):
    vec = {}
    for term, freq in tf.items():
        if term in idf:
            vec[term] = freq * idf[term]
    return vec


def cosine_similarity(v1, v2):
    dot = sum(v1[t] * v2.get(t, 0) for t in v1)
    norm1 = math.sqrt(sum(v * v for v in v1.values()))
    norm2 = math.sqrt(sum(v * v for v in v2.values()))

    if norm1 == 0 or norm2 == 0:
        return 0.0

    return dot / (norm1 * norm2)
