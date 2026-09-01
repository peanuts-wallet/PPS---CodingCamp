from collections import Counter


def solution(clothes):
    category_counts = Counter(category for _, category in clothes)
    combination_count = 1

    for count in category_counts.values():
        combination_count *= count + 1

    return combination_count - 1
