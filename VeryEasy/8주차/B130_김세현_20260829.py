def solution(numbers, target):
    def search(index, total):
        if index == len(numbers):
            return int(total == target)

        return search(index + 1, total + numbers[index]) + search(
            index + 1, total - numbers[index]
        )

    return search(0, 0)
