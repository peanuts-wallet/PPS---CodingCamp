class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = "".join(str(digit) for digit in digits)
        number = int(number)
        number += 1
        digits = [int(digit) for digit in str(number)]
        return digits