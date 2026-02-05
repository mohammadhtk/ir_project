# src/compression.py
from typing import Dict, List

def gap_encode(postings: List[int]) -> List[int]:
    """Gap encoding برای لیست doc_idهای مرتب."""
    if not postings:
        return []
    gaps = [postings[0]]
    for i in range(1, len(postings)):
        gaps.append(postings[i] - postings[i - 1])
    return gaps

def gap_decode(gaps: List[int]) -> List[int]:
    """بازیابی doc_idها از gap encoding."""
    postings = []
    total = 0
    for gap in gaps:
        total += gap
        postings.append(total)
    return postings

def compress_inverted_index(inverted_index: Dict[str, List[int]]) -> Dict[str, List[int]]:
    """فشرده‌سازی کل نمایه معکوس با gap encoding."""
    return {term: gap_encode(sorted(postings)) for term, postings in inverted_index.items()}

def decompress_inverted_index(compressed_index: Dict[str, List[int]]) -> Dict[str, List[int]]:
    """بازیابی نمایه از حالت فشرده."""
    return {term: gap_decode(gaps) for term, gaps in compressed_index.items()}