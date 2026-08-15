def solution(n, lost, reserve):
    clothes = [1] * (n + 1)

    for x in lost:
        clothes[x] -= 1

    for x in reserve:
        clothes[x] += 1

    for i in range(1, n + 1):
        if clothes[i] == 0:
            if i > 1 and clothes[i - 1] == 2:
                clothes[i - 1] -= 1
                clothes[i] += 1
            elif i < n and clothes[i + 1] == 2:
                clothes[i + 1] -= 1
                clothes[i] += 1

    return sum(1 for i in range(1, n + 1) if clothes[i] >= 1)