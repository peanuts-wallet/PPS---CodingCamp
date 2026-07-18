class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        answer = 0
        n = len(arr)
        
        for start in range(n):
            current_sum = 0
            
            for end in range(start, n):
                current_sum += arr[end]
