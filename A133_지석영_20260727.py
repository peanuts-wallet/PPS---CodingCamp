# A133 Capitalize the Title
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split()
        answer = []

        for word in words:
            word = word.lower()

            if len(word) > 2:
                word = word.capitalize()

            answer.append(word)

        return ' '.join(answer)
