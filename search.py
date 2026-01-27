from preprocess import preprocess
from vector_model import (
    compute_tf,
    compute_tfidf,
    cosine_similarity
)

def search(query, docs_tf, idf, top_k=5):
    query_tokens = preprocess(query)
    query_tf = compute_tf(query_tokens)
    query_vec = compute_tfidf(query_tf, idf)

    scores = {}

    for doc_id, tf in docs_tf.items():
        doc_vec = compute_tfidf(tf, idf)
        score = cosine_similarity(query_vec, doc_vec)
        scores[doc_id] = score

    ranked = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return ranked[:top_k]
