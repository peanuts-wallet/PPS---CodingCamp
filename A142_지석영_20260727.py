# A142 같은 숫자는 싫어
def solution(arr):
    answer = []

    for number in arr:
        if not answer or answer[-1] != number:
            answer.append(number)

    return answer

