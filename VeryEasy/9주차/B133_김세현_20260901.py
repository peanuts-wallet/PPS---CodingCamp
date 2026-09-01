from collections import deque


def solution(begin, target, words):
    remaining_words = set(words)

    if target not in remaining_words:
        return 0

    queue = deque([(begin, 0)])

    while queue:
        current_word, step = queue.popleft()

        for next_word in list(remaining_words):
            difference_count = sum(
                current != next_ for current, next_ in zip(current_word, next_word)
            )

            if difference_count != 1:
                continue
            if next_word == target:
                return step + 1

            remaining_words.remove(next_word)
            queue.append((next_word, step + 1))

    return 0
