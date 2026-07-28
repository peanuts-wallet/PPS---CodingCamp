# A162 카드 뭉치
def solution(cards1, cards2, goal):
    first_index = 0
    second_index = 0

    for word in goal:
        if (
            first_index < len(cards1)
            and cards1[first_index] == word
        ):
            first_index += 1

        elif (
            second_index < len(cards2)
            and cards2[second_index] == word
        ):
            second_index += 1

        else:
            return "No"

    return "Yes"

