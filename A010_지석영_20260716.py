# A010 문자열 압축
def solution(s):
    if len(s) == 1:
        return 1

    answer = len(s)

    for unit in range(1, len(s) // 2 + 1):
        compressed = ""
        previous = s[:unit]
        count = 1

        for start in range(unit, len(s), unit):
            current = s[start:start + unit]

            if current == previous:
                count += 1
            else:
                if count > 1:
                    compressed += str(count)

                compressed += previous
                previous = current
                count = 1

        if count > 1:
            compressed += str(count)

        compressed += previous
        answer = min(answer, len(compressed))

    return answer
