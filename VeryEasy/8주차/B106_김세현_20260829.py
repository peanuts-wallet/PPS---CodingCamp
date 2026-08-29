def solution(arr):
    def gcd(first, second):
        while second:
            first, second = second, first % second

        return first

    least_common_multiple = 1

    for number in arr:
        least_common_multiple = least_common_multiple * number // gcd(
            least_common_multiple, number
        )

    return least_common_multiple
