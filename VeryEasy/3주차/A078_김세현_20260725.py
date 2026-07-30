def solution(citations):
    citations.sort(reverse=True)

    for i, citation in enumerate(citations):
        h = i + 1

        if citation < h:
            return i

    return len(citations)