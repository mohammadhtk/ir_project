# Information Retrieval Course Project

## 📌 Project Overview
This project is a **simple Information Retrieval (IR) system** implemented in Python as the final project for the *Information Retrieval* course.

The system retrieves relevant text documents from a collection of `.txt` files based on a user query, ranks them using the **Vector Space Model**, and evaluates performance using **Precision@k**.  
It also includes **inverted index compression** and **query expansion**.

---

## ✨ Features
- Text preprocessing (lowercase, punctuation removal, tokenization, optional stemming)
- Dictionary construction (term → document frequency)
- Inverted Index construction
- Inverted Index compression using **Gap Encoding**
- Vector Space Model (TF, IDF, TF-IDF)
- Cosine similarity–based document ranking
- Top-k document retrieval
- Query Expansion using manual synonyms
- Interactive CLI search
- System evaluation using Precision@k
- Evaluation report generation

---

## 🛠 Technologies & Libraries
- **Python 3**
- Allowed libraries only:
  - `math`
  - `collections`
  - `json`
  - `nltk` (only for simple stemming/tokenization)

❌ No search engines or IR libraries such as Elasticsearch, Lucene, or Whoosh are used.

---

## 📂 Project Structure

```
ir_project/
│
├── docs/                     # Text documents (.txt)
├── config/
│   ├── synonyms.txt          # Synonyms for query expansion
│   └── queries.json          # Test queries for evaluation
│
├── output/
│   └── evaluation_report.txt # Evaluation results
│
├── src/
│   ├── preprocessing.py     # Text preprocessing
│   ├── indexing.py          # Dictionary & inverted index
│   ├── compression.py       # Gap encoding & compression
│   ├── vector_model.py      # TF, IDF, TF-IDF, cosine similarity
│   ├── search.py             # Vector space search
│   ├── search_compressed.py # Search on compressed index
│   ├── query_expansion.py   # Query expansion
│   ├── evaluate.py          # Precision@k evaluation
│   └── cli_logger.py        # CLI query logging
│
├── main.py                   # Main execution pipeline
├── requirements.txt
└── README.md
```

---

## ⚙️ Preprocessing Steps
Each document and query undergoes the same preprocessing:
1. Convert text to lowercase
2. Remove punctuation and non-alphabetic characters
3. Tokenization
4. Optional stemming using Porter Stemmer

---

## 📚 Dictionary & Inverted Index
- **Dictionary** stores:
```

term → document frequency (df)

```
- **Inverted Index** stores:
```

term → [docID1, docID2, ...]

```

Document IDs are numeric internally, while filenames are used for display.

---

## 🗜 Inverted Index Compression
- **Gap Encoding** is used to compress posting lists
- Differences between sorted document IDs are stored
- Decompression is supported for searching

---

## 📐 Vector Space Model
- Term Frequency (TF)
- Inverse Document Frequency (IDF)
- TF-IDF weighting
- Cosine similarity for ranking
- Top-k relevant documents returned

---

## 🔎 Query Expansion
- Manual synonyms loaded from `config/synonyms.txt`
- Query terms are expanded before re-running search
- Results before and after expansion can be compared

---

## 📊 Evaluation
- At least **3 test queries**
- Manually defined relevant documents
- Evaluation metric: **Precision@k**
- Results saved in:
```

output/evaluation_report.txt

````

---

## 🖥 Interactive CLI Search
Run the project and search interactively:

```bash
python main.py
````

Type queries in the terminal.
Type `exit` to quit.

---

## 🧪 Running Evaluation

Evaluation queries are loaded from:

```
config/queries.json
```

Each query includes:

```json
{
  "query": "weather",
  "relevant_docs": ["doc1.txt", "doc2.txt"]
}
```

---

## ✅ Output

* Ranked Top-k documents per query
* Precision@k values
* Comparison before and after query expansion

---

## 📌 Notes

* This project is fully implemented **from scratch**
* Designed strictly according to course requirements
* Intended for educational and academic purposes

---

## 👤 Contributors

[MohammadhTk](https://github.com/mohammadhtk)

[HoesienZR](https://github.com/HoesienZR)




