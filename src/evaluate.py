# src/evaluate.py
from typing import List, Tuple, Dict, Set
from .query_expansion import expand_query
import json

def precision_at_k(ranked_results: List[Tuple[str, float]], relevant_docs: Set[str], k: int) -> float:
    top_k = [doc_id for doc_id, _ in ranked_results[:k]]
    return sum(1 for doc in top_k if doc in relevant_docs) / k

def save_evaluation_report(
    test_queries: List[Dict],
    results_before: List[List[Tuple[str, float]]],
    results_after: List[List[Tuple[str, float]]],
    output_path: str,
    k: int
):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("Information Retrieval - Final Evaluation Report\n")
        f.write("=" * 60 + "\n\n")
        for i, tq in enumerate(test_queries):
            f.write(f"Query: {tq['query']}\n")
            f.write(f"Relevant Docs: {tq['relevant_docs']}\n\n")
            f.write(f"Top-{k} BEFORE Expansion:\n")
            for j, (doc, score) in enumerate(results_before[i]):
                f.write(f"  {j+1}. {doc} | {score:.4f}\n")
            f.write(f"\nTop-{k} AFTER Expansion:\n")
            for j, (doc, score) in enumerate(results_after[i]):
                f.write(f"  {j+1}. {doc} | {score:.4f}\n")
            f.write("\n" + "-" * 60 + "\n")
    print(f"✅ Report saved to {output_path}")

def run_evaluation(
    test_queries: List[Dict],
    search_func,
    inverted_index: dict,
    idf: dict,
    docs_tf: dict,
    doc_ids: List[str],
    synonyms_dict: Dict[str, List[str]],
    k: int = 5,
    output_file: str = "output/evaluation_report.txt"
):
    results_before, results_after = [], []
    for tq in test_queries:
        query = tq["query"]
        relevant = set(tq["relevant_docs"])
        # Before expansion
        res_before = search_func(query, inverted_index, idf, docs_tf, doc_ids, top_k=k)
        results_before.append(res_before)
        # After expansion
        expanded_query = expand_query(query, synonyms_dict)
        res_after = search_func(expanded_query, inverted_index, idf, docs_tf, doc_ids, top_k=k)
        results_after.append(res_after)
    save_evaluation_report(test_queries, results_before, results_after, output_file, k)