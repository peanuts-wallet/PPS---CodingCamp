# A145 부족한 금액 계산하기
def solution(price, money, count):
    total_cost = price * count * (count + 1) // 2
    shortage = total_cost - money

    if shortage > 0:
        return shortage

    return 0
