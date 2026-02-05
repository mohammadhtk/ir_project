# src/preprocessing.py
import re
from typing import List
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

def simple_preprocess(text: str, use_stemming: bool = True) -> List[str]:
    """پیش‌پردازش متن: lowercase + حذف علائم + توکن‌سازی + (اختیاری) stemming"""
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)  # حذف غیرالفبا
    tokens = text.split()
    if use_stemming:
        tokens = [stemmer.stem(token) for token in tokens]
    return tokens

def load_and_preprocess_documents(folder_path: str, use_stemming: bool = True) -> tuple:
    """بارگذاری و پیش‌پردازش تمام اسناد در پوشه"""
    from os import listdir
    from os.path import join

    documents = {}
    doc_ids = []
    for idx, filename in enumerate(sorted(listdir(folder_path))):
        if filename.endswith(".txt"):
            with open(join(folder_path, filename), 'r', encoding='utf-8') as f:
                raw_text = f.read()
            documents[idx] = simple_preprocess(raw_text, use_stemming)
            doc_ids.append(filename)  # استفاده از نام فایل به عنوان docID
    return documents, doc_ids