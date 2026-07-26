# A166 크기가 작은 부분 문자열
def solution(t, p):
    answer = 0
    length = len(p)
    p_number = int(p)

    for start in range(len(t) - length + 1):
        part = t[start:start + length]
        part_number = int(part)

        if part_number <= p_number:
            answer += 1

    return answer

