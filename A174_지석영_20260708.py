# A174 명예의 전당 (1)
def solution(k, score):
    answer = []
    hall_of_fame = []

    for current_score in score:
        hall_of_fame.append(current_score)
        hall_of_fame.sort(reverse=True)

        if len(hall_of_fame) > k:
            hall_of_fame.pop()

        answer.append(hall_of_fame[-1])

    return answer

