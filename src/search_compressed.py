# src/search_compressed.py
from typing import List
from src.preprocessing import simple_preprocess


def decompress_postings(gaps):
    docs = []
    current = 0
    for gap in gaps:
        current += gap
        docs.append(current)
    return docs


def compressed_vector_space_search(
    query: str,
    compressed_index: dict,
    idf: dict,
    docs_tf: dict,
    doc_ids: List[str],
    top_k: int = 5
):
    # CHANGED: پیش‌پردازش query مثل بقیه سیستم
    query_tokens = simple_preprocess(query)

    # بازسازی inverted index فقط برای termهای query
    inverted_index = {}

    for term in query_tokens:
        if term in compressed_index:
            inverted_index[term] = decompress_postings(
                compressed_index[term]
            )

    # استفاده از همان vector space search
    from src.search import vector_space_search
    return vector_space_search(
        query,
        inverted_index,
        idf,
        docs_tf,
        doc_ids,
        top_k=top_k
    )
