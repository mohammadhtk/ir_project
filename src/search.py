# src/search.py
from typing import List, Tuple
from preprocessing import simple_preprocess
from vector_model import compute_tf, compute_tfidf, cosine_similarity

def vector_space_search(
    query: str,
    inverted_index: dict,
    idf: dict,
    docs_tf: dict,
    doc_ids: List[str],
    top_k: int = 5
) -> List[Tuple[str, float]]:
    query_tokens = simple_preprocess(query)
    query_tf = compute_tf(query_tokens)
    query_vec = compute_tfidf(query_tf, idf)

    scores = {}
    for doc_id in doc_ids:
        doc_numeric_id = doc_ids.index(doc_id)  # تبدیل نام فایل به عدد برای دسترسی به docs_tf
        doc_vec = compute_tfidf(docs_tf[doc_numeric_id], idf)
        score = cosine_similarity(query_vec, doc_vec)
        scores[doc_id] = score

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return ranked[:top_k]