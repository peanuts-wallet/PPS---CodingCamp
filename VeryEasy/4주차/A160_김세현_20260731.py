def solution(n, m, section):
    answer = 0
    painted_until = 0

    for start in section:
        if start > painted_until:
            answer += 1
            painted_until = start + m - 1

    return answer