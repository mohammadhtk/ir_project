import re
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

def preprocess(text, use_stemming=True):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    tokens = text.split()

    if use_stemming:
        tokens = [stemmer.stem(token) for token in tokens]

    return tokens
