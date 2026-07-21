class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        exchange = [0, 0, 0]  # 5, 10, 20달러 지폐 개수

        for bill in bills:
            if bill == 5:
                exchange[0] += 1
            elif bill == 10:
                if exchange[0] == 0:
                    return False
                exchange[0] -= 1
                exchange[1] += 1
            else:  # bill == 20
                if exchange[1] >= 1 and exchange[0] >= 1:
                    exchange[1] -= 1
                    exchange[0] -= 1
                elif exchange[0] >= 3:
                    exchange[0] -= 3
                else:
                    return False
                exchange[2] += 1
        return True