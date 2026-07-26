# A079 K번째수
def solution(array, commands):
    answer = []

    for command in commands:
        start = command[0]
        end = command[1]
        position = command[2]

        sliced = array[start - 1:end]
        sliced.sort()

        answer.append(sliced[position - 1])

    return answer

