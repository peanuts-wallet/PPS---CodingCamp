# A147 행렬의 덧셈
def solution(arr1, arr2):
    answer = []

    for row in range(len(arr1)):
        new_row = []

        for column in range(len(arr1[row])):
            value = arr1[row][column] + arr2[row][column]
            new_row.append(value)

        answer.append(new_row)

    return answer

