def solution(answers):
    patterns = (
        (1, 2, 3, 4, 5),
        (2, 1, 2, 3, 2, 4, 2, 5),
        (3, 3, 1, 1, 2, 2, 4, 4, 5, 5),
    )
    scores = [0, 0, 0]

    for index, answer in enumerate(answers):
        for person, pattern in enumerate(patterns):
            if answer == pattern[index % len(pattern)]:
                scores[person] += 1

    highest_score = max(scores)

    return [person + 1 for person, score in enumerate(scores) if score == highest_score]
