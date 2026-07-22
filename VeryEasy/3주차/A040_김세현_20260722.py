class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # 둘로 슬라이싱해서 저장하기
        # 각각 vowel count에 저장해서 비교하기
        # 길이가 4라면 슬라이싱 범위: [0:2], [2:4] -> [0:mid+1], [mid:length]
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        mid = len(s)//2
        length = len(s)
        string1 = s[0:mid]
        string2 = s[mid:length]
        count1 = 0
        count2 = 0
        for char in string1:
            if char in vowel:
                count1 += 1
        for char in string2:
            if char in vowel:
                count2 += 1
        if count1 == count2:
            return True
        else:
            return False