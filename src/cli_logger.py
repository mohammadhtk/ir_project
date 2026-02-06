from typing import List, Tuple

def log_cli_query(
    query: str,
    results: List[Tuple[str, float]],
    output_path: str = "output/cli_queries_log.txt",
    top_k: int = 5
):
    with open(output_path, "a", encoding="utf-8") as f:
        f.write(f"Query: {query}\n")
        f.write(f"Top-{top_k} Results:\n")
        for i, (doc, score) in enumerate(results):
            f.write(f"  {i+1}. {doc} | {score:.4f}\n")
        f.write("-" * 50 + "\n")
