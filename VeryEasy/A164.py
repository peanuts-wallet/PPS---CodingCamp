def solution(s):
    answer = []
    last_position = {}

    for i, char in enumerate(s):
        if char in last_position:
            answer.append(i - last_position[char])
        else:
            answer.append(-1)

        last_position[char] = i

    return answer