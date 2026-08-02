def solution(babbling):
    answer = 0
    sounds = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        index = 0
        previous = ""

        while index < len(word):
            matched = False

            for sound in sounds:
                if word.startswith(sound, index) and sound != previous:
                    index += len(sound)
                    previous = sound
                    matched = True
                    break

            if not matched:
                break
        if index == len(word):
            answer += 1

    return answer