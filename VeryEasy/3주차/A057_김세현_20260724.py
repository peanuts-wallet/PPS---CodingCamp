def solution(cookie):
    answer = 0
    n = len(cookie)

    # m과 m+1 사이를 두 아들의 경계로 설정
    for m in range(n - 1):
        left = m
        right = m + 1

        left_sum = cookie[left]
        right_sum = cookie[right]

        while left >= 0 and right < n:
            if left_sum == right_sum:
                answer = max(answer, left_sum)

            # 합이 작은 쪽의 범위를 확장
            if left_sum <= right_sum:
                left -= 1

                if left >= 0:
                    left_sum += cookie[left]
            else:
                right += 1

                if right < n:
                    right_sum += cookie[right]

    return answer