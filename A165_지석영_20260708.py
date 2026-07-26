# A165 기사단원의 무기
def solution(number, limit, power):
    answer = 0

    for knight in range(1, number + 1):
        divisor_count = 0
        divisor = 1

        # 제곱근까지만 확인하여 약수 개수 계산
        while divisor * divisor <= knight:
            if knight % divisor == 0:
                divisor_count += 1

                # 제곱수인 경우 같은 약수를 한 번만 계산
                if divisor * divisor != knight:
                    divisor_count += 1

            divisor += 1

        if divisor_count > limit:
            answer += power
        else:
            answer += divisor_count

    return answer

