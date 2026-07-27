class Solution:
    def dayOfYear(self, date: str) -> int:
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])
        
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            month_days[1] = 29
        
        answer = 0
        
        for i in range(month - 1):
            answer += month_days[i]
        
        answer += day
        
        return answer