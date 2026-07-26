# A161 대충 만든 자판
def solution(keymap, targets):
    answer = []
    min_press = {}

    # 각 문자를 입력하기 위한 최소 누름 횟수 저장
    for key in keymap:
        for index in range(len(key)):
            character = key[index]
            press_count = index + 1

            if character not in min_press:
                min_press[character] = press_count
            elif press_count < min_press[character]:
                min_press[character] = press_count

    for target in targets:
        total = 0
        possible = True

        for character in target:
            if character not in min_press:
                possible = False
                break

            total += min_press[character]

        if possible:
            answer.append(total)
        else:
            answer.append(-1)

    return answer

