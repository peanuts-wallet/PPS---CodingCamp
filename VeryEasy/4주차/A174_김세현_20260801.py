def solution(k, score):
    answer = []
    hall = []

    for current_score in score:
        hall.append(current_score)
        hall.sort(reverse=True)

        if len(hall) > k:
            hall.pop()

        answer.append(hall[-1])

    return answer