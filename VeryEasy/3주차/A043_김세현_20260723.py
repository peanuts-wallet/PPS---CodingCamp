class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix_count = 0
        min_length = min(len(word) for word in strs)

        for i in range(min_length):
            same = True

            for word in strs:
                if word[i] != strs[0][i]:
                    same = False
                    break
            if same:
                prefix_count += 1
            else:
                break
        return strs[0][:prefix_count]