# A009 문자열 다루기 기본
def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False

    for character in s:
        if character < "0" or character > "9":
            return False

    return True
