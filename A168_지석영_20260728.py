# A168 과일 장수
def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0

    for index in range(m - 1, len(score), m):
        lowest_score = score[index]
        answer += lowest_score * m

    return answer

