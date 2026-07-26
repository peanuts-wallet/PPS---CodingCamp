# A075 가장 큰 수
from functools import cmp_to_key


def solution(numbers):
    string_numbers = []

    for number in numbers:
        string_numbers.append(str(number))

    def compare(first, second):
        if first + second > second + first:
            return -1
        elif first + second < second + first:
            return 1
        else:
            return 0

    string_numbers.sort(key=cmp_to_key(compare))

    answer = ''.join(string_numbers)

    if answer[0] == '0':
        return '0'

    return answer
