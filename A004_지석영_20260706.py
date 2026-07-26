# A004 나누어 떨어지는 숫자 배열
def solution(arr, divisor):
    answer = []

    for number in arr:
        if number % divisor == 0:
            answer.append(number)

    if len(answer) == 0:
        return [-1]

    answer.sort()
    return answer
