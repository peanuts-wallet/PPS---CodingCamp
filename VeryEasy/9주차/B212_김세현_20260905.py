def solution(s, n):
    encrypted = []

    for character in s:
        if character == " ":
            encrypted.append(character)
            continue

        alphabet_start = ord("A") if character.isupper() else ord("a")
        shifted = (ord(character) - alphabet_start + n) % 26
        encrypted.append(chr(alphabet_start + shifted))

    return "".join(encrypted)
