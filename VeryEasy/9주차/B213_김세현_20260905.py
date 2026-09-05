def solution(s):
    converted_words = []

    for word in s.split(" "):
        converted_word = "".join(
            character.upper() if index % 2 == 0 else character.lower()
            for index, character in enumerate(word)
        )
        converted_words.append(converted_word)

    return " ".join(converted_words)
