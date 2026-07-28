# A167 푸드 파이트 대회
def solution(food):
    left_side = ""

    for food_number in range(1, len(food)):
        count = food[food_number] // 2
        left_side += str(food_number) * count

    right_side = left_side[::-1]

    return left_side + "0" + right_side

