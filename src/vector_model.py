# src/vector_model.py
import math
from collections import defaultdict
from typing import Dict, List

def compute_tf(tokens: List[str]) -> Dict[str, int]:
    tf = defaultdict(int)
    for token in tokens:
        tf[token] += 1
    return dict(tf)

def compute_all_tf(documents: Dict[int, List[str]]) -> Dict[int, Dict[str, int]]:
    return {doc_id: compute_tf(tokens) for doc_id, tokens in documents.items()}

def compute_idf(dictionary: Dict[str, int], N: int) -> Dict[str, float]:
    return {term: math.log(N / df) for term, df in dictionary.items()}

def compute_tfidf(tf: Dict[str, int], idf: Dict[str, float]) -> Dict[str, float]:
    return {term: freq * idf.get(term, 0) for term, freq in tf.items() if term in idf}

def cosine_similarity(v1: Dict[str, float], v2: Dict[str, float]) -> float:
    dot = sum(v1[t] * v2.get(t, 0) for t in v1)
    norm1 = math.sqrt(sum(v * v for v in v1.values()))
    norm2 = math.sqrt(sum(v * v for v in v2.values()))
    return dot / (norm1 * norm2) if norm1 * norm2 != 0 else 0.0