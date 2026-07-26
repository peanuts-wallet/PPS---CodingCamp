# A164 가장 가까운 같은 글자
def solution(s):
    answer = []
    last_position = {}

    for index in range(len(s)):
        character = s[index]

        if character not in last_position:
            answer.append(-1)
        else:
            distance = index - last_position[character]
            answer.append(distance)

        # 현재 위치를 가장 최근 위치로 저장
        last_position[character] = index

    return answer

