# A146 최솟값 만들기
def solution(A, B):
    A.sort()
    B.sort(reverse=True)

    answer = 0

    for index in range(len(A)):
        answer += A[index] * B[index]

    return answer

