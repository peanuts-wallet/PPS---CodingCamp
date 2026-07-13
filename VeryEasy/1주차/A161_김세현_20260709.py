def solution(keymap, targets):
    answer = []
    min_press = {}
    for keys in keymap:
        for i, char in enumerate(keys):
            press_count = i + 1

            if char not in min_press:
                min_press[char] = press_count
            else:
                min_press[char] = min(min_press[char], press_count)
    for target in targets:
        total = 0

        for char in target:
            if char not in min_press:
                total = -1
                break

            total += min_press[char]

        answer.append(total)

    return answer