# A006 문자열 내 p와 y의 개수
def solution(s):
    p_count = 0
    y_count = 0

    for character in s.lower():
        if character == "p":
            p_count += 1
        elif character == "y":
            y_count += 1

    return p_count == y_count
