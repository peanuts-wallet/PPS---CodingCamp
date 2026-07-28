# A140 폰켓몬
def solution(nums):
    maximum_count = len(nums) // 2
    type_count = len(set(nums))

    return min(maximum_count, type_count)

