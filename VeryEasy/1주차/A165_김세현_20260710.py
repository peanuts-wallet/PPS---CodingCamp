def solution(number, limit, power):
    answer = 0

    for num in range(1, number + 1):
        divisor_count = 0

        # num의 약수 개수 구하기
        for i in range(1, int(num ** 0.5) + 1):
            if num % i == 0:
                if i * i == num:
                    divisor_count += 1
                else:
                    divisor_count += 2

        if divisor_count > limit:
            answer += power
        else:
            answer += divisor_count

    return answer