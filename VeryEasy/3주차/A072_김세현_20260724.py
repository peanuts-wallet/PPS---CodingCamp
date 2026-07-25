class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = map(int, date.split('-'))

        days_in_month = [
            31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31
        ]

        answer = sum(days_in_month[:month - 1]) + day

        is_leap = (
            year % 400 == 0
            or (year % 4 == 0 and year % 100 != 0)
        )

        if is_leap and month > 2:
            answer += 1

        return answer
