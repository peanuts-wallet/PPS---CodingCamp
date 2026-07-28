# A169 햄버거 만들기
def solution(ingredient):
    answer = 0
    stack = []

    for current_ingredient in ingredient:
        stack.append(current_ingredient)

        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            del stack[-4:]
            answer += 1

    return answer

