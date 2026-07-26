# A175 옹알이 (2)
def solution(babbling):
    answer = 0
    sounds = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        position = 0
        previous_sound = ""
        possible = True

        while position < len(word):
            found_sound = False

            for sound in sounds:
                if word.startswith(sound, position):
                    if sound == previous_sound:
                        possible = False
                        break

                    previous_sound = sound
                    position += len(sound)
                    found_sound = True
                    break

            if not possible:
                break

            if not found_sound:
                possible = False
                break

        if possible:
            answer += 1

    return answer

