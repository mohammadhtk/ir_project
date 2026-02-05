def save_results_to_file(filename, test_queries, all_results_before, all_results_after, k=5):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("IR Project - Final Evaluation Report\n")
        f.write("=" * 50 + "\n\n")
        for i, tq in enumerate(test_queries):
            f.write(f"Query: {tq['query']}\n")
            f.write(f"Relevant: {tq['relevant_docs']}\n\n")

            f.write(f"Top-{k} BEFORE expansion:\n")
            for j, (doc, score) in enumerate(all_results_before[i]):
                f.write(f"  {j + 1}. {doc} | {score:.4f}\n")

            f.write(f"\nTop-{k} AFTER expansion:\n")
            for j, (doc, score) in enumerate(all_results_after[i]):
                f.write(f"  {j + 1}. {doc} | {score:.4f}\n")

            f.write("\n" + "-" * 50 + "\n")
    print(f"\n✅ Results saved to {filename}")