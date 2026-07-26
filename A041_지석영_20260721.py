# A041 JadenCase 문자열 만들기
def solution(s):
    words = s.split(' ')
    answer = []

    for word in words:
        answer.append(word.capitalize())

    return ' '.join(answer)

