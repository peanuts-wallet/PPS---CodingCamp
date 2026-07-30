class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        month_days = [31,28,31,30,31,30,31,31,30,31,30,31]

        total = 0

        for y in range(1971, year):
            total += 365
            if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
                total += 1

        for m in range(month - 1):
            total += month_days[m]

        if month > 2 and ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)):
            total += 1

        total += day - 1

        return days[total % 7]