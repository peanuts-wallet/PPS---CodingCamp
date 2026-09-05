class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        lowest, second_lowest = sorted(prices)[:2]
        remaining_money = money - lowest - second_lowest

        return remaining_money if remaining_money >= 0 else money
