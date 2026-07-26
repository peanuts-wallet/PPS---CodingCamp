# A027 큰 수 만들기
def solution(number, k):
    stack = []

    for digit in number:
        while stack and k > 0 and stack[-1] < digit:
            stack.pop()
            k -= 1

        stack.append(digit)

    # 제거 횟수가 남으면 뒤에서 제거
    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)

