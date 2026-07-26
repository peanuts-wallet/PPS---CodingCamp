# A042 Backspace String Compare
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def make_string(text):
            stack = []

            for character in text:
                if character == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(character)

            return ''.join(stack)

        return make_string(s) == make_string(t)

