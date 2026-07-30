class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        total = 0
        
        for y in range(1971, year):
            if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
                total += 366
            else:
                total += 365
        
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            month_days[1] = 29
        
        for m in range(month - 1):
            total += month_days[m]
        
        total += day - 1
        
        return week[total % 7]