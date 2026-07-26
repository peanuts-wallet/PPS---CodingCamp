# A273 Shuffle String
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        answer = [''] * len(s)

        for index in range(len(s)):
            new_position = indices[index]
            answer[new_position] = s[index]

        return ''.join(answer)

