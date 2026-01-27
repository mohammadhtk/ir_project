from indexer import load_documents, build_dictionary
from vector_model import compute_all_tf, compute_idf
from search import search
from evaluation import precision_at_k

DOC_PATH = "docs"

# Load and index documents
documents = load_documents(DOC_PATH)
dictionary = build_dictionary(documents)
docs_tf = compute_all_tf(documents)
idf = compute_idf(dictionary, len(documents))


# Test Queries (minimum 3)
queries = [
    "weather",
    "morning",
    "music",
]

# Manually defined relevant documents
relevance_judgments = {
    0: {0, 1},      # relevant docs for query 1
    1: {2},         # relevant docs for query 2
    2: {1, 3}       # relevant docs for query 3
}

k = 10

for i, query in enumerate(queries):
    results = search(query, docs_tf, idf, top_k=k)

    print(f"\nQuery {i+1}: {query}")
    print("Top-k Results:")
    for doc_id, score in results:
        print(f"Doc {doc_id}  Score: {score:.4f}")

    precision = precision_at_k(results, relevance_judgments[i], k)
    print(f"Precision@{k}: {precision:.2f}")
