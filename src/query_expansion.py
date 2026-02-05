# src/query_expansion.py
from typing import Dict
from preprocessing import simple_preprocess
from typing import List
def load_synonyms(file_path: str) -> Dict[str, List[str]]:
    synonyms = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if '->' in line:
                    term, syns = line.split('->', 1)
                    term = term.strip().lower()
                    syn_list = [s.strip().lower() for s in syns.split(',')]
                    synonyms[term] = syn_list
    except FileNotFoundError:
        print(f"⚠️ Synonym file not found: {file_path}")
    return synonyms

def expand_query(query: str, synonyms_dict: Dict[str, List[str]], max_expansions: int = 2) -> str:
    tokens = simple_preprocess(query)
    expanded = []
    seen = set()
    for token in tokens:
        if token not in seen:
            expanded.append(token)
            seen.add(token)
        if token in synonyms_dict:
            for syn in synonyms_dict[token][:max_expansions]:
                if syn not in seen:
                    expanded.append(syn)
                    seen.add(syn)
    return ' '.join(expanded)