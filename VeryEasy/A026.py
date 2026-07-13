def solution(x):
    answer = True
    length = len(str(x))
    hashad = 0
    for i in range(length, 0, -1):
        if (i == 1):
            hashad += (x % 10)
        else:
            hashad += (x // (10 ** (i - 1))) % 10
    if x % hashad != 0: answer = False
    # print(f'hashad number: {hashad}')
    return answer