import re

def load_synonyms(file_path):
    synonyms = {}
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
    return synonyms