# A144 모음사전
def solution(word):
    vowels = "AEIOU"
    weights = [781, 156, 31, 6, 1]
    answer = 0

    for index in range(len(word)):
        vowel_index = vowels.index(word[index])
        answer += vowel_index * weights[index] + 1

    return answer

