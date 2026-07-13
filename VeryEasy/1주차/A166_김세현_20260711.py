def solution(t, p):
    answer = 0
    length = len(p)
    p_number = int(p)

    for i in range(len(t) - length + 1):
        part = t[i:i + length]

        if int(part) <= p_number:
            answer += 1

    return answer