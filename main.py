# main.py
from src.preprocessing import load_and_preprocess_documents
from src.indexing import build_dictionary, build_inverted_index
from src.vector_model import compute_all_tf, compute_idf
from src.search import vector_space_search
from src.query_expansion import load_synonyms
from src.evaluate import run_evaluation
from src.compression import compress_inverted_index  # شما قبلاً gap_encode را پیاده کردید

# === CONFIGURATION ===
DOC_DIR = "docs"
SYNONYM_FILE = "config/synonyms.txt"

TEST_QUERIES = [
    {"query": "weather", "relevant_docs": ["doc1.txt", "doc2.txt"]},
    {"query": "morning", "relevant_docs": ["doc3.txt"]},
    {"query": "music", "relevant_docs": ["doc4.txt", "doc5.txt"]}
]

TOP_K = 5
OUTPUT_DIR = "output"

# === PIPELINE ===
if __name__ == "__main__":
    print("🔄 Loading and preprocessing documents...")
    documents, doc_ids = load_and_preprocess_documents(DOC_DIR)

    print("📚 Building dictionary and inverted index...")
    dictionary = build_dictionary(documents)
    inverted_index = build_inverted_index(documents)  # CHANGED: حذف doc_ids

    compressed_index = compress_inverted_index(inverted_index)

    print("📊 Computing TF-IDF...")
    docs_tf = compute_all_tf(documents)
    idf = compute_idf(dictionary, len(documents))

    print("🔍 Loading synonyms...")
    synonyms = load_synonyms(SYNONYM_FILE)

    print("📈 Running evaluation...")
    run_evaluation(
        test_queries=TEST_QUERIES,
        search_func=vector_space_search,
        inverted_index=inverted_index,
        idf=idf,
        docs_tf=docs_tf,
        doc_ids=doc_ids,
        synonyms_dict=synonyms,
        k=TOP_K,
        output_file=f"{OUTPUT_DIR}/evaluation_report.txt"
    )