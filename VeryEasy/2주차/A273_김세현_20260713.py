class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        answer = [0 for x in range(len(s))]
        for i in range(len(s)):
            answer[indices[i]] = s[i]
        final_answer = "".join(answer)
        return final_answer