class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        answer = []
        
        for num in range(left, right + 1):
            is_self_dividing = True
            
            for digit in str(num):
                digit = int(digit)
                
                if digit == 0 or num % digit != 0:
                    is_self_dividing = False
                    break
            
            if is_self_dividing:
                answer.append(num)
        
        return answer