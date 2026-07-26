# A057 쿠키 구입
def solution(cookie):
    answer = 0

    # 두 구간의 경계
    for middle in range(len(cookie) - 1):
        left = middle
        right = middle + 1

        left_sum = cookie[left]
        right_sum = cookie[right]

        while True:
            if left_sum == right_sum:
                answer = max(answer, left_sum)

            if left_sum <= right_sum:
                left -= 1

                if left < 0:
                    break

                left_sum += cookie[left]

            else:
                right += 1

                if right >= len(cookie):
                    break

                right_sum += cookie[right]

    return answer

