def gap_encode(postings):
    postings = sorted(postings)
    if not postings:
        return []

    gaps = [postings[0]]
    for i in range(1, len(postings)):
        gaps.append(postings[i] - postings[i - 1])
    return gaps


def gap_decode(gaps):
    postings = []
    total = 0
    for gap in gaps:
        total += gap
        postings.append(total)
    return postings


def compress_inverted_index(inverted_index):
    compressed = {}
    for term, postings in inverted_index.items():
        compressed[term] = gap_encode(postings)
    return compressed
