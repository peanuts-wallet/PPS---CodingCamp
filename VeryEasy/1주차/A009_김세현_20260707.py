def solution(s):
    answer = False
    length = len(s)
    # 문자열 길이 판별
    if (length != 4 and length != 6):
        return False
    if not s.isdigit():
        return False
    return True