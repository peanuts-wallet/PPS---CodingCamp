# A143 올바른 괄호
def solution(s):
    count = 0

    for parenthesis in s:
        if parenthesis == '(':
            count += 1
        else:
            count -= 1

        if count < 0:
            return False

    return count == 0
