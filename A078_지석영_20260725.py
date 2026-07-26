# A078 H-Index
def solution(citations):
    citations.sort(reverse=True)

    for index in range(len(citations)):
        h = index + 1

        if citations[index] < h:
            return index

    return len(citations)

