def solution(price, money, count):
    total_price = 0

    for i in range(1, count + 1):
        total_price += i * price

    return max(total_price - money, 0)