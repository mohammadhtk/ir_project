def precision_at_k(ranked_results, relevant_docs, k):

    top_k_docs = [doc_id for doc_id, _ in ranked_results[:k]]

    relevant_count = 0
    for doc_id in top_k_docs:
        if doc_id in relevant_docs:
            relevant_count += 1

    return relevant_count / k

