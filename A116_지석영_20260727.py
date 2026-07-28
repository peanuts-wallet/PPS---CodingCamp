# A116 Day of the Week
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        week_days = [
            "Friday",
            "Saturday",
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday"
        ]

        month_days = [
            31, 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31
        ]

        total_days = 0

        # 1971년부터 입력 연도 전까지의 날짜 수
        for current_year in range(1971, year):
            if (
                current_year % 400 == 0
                or (
                    current_year % 4 == 0
                    and current_year % 100 != 0
                )
            ):
                total_days += 366
            else:
                total_days += 365

        # 입력 연도가 윤년이면 2월을 29일로 설정
        if (
            year % 400 == 0
            or (year % 4 == 0 and year % 100 != 0)
        ):
            month_days[1] = 29

        for current_month in range(month - 1):
            total_days += month_days[current_month]

        total_days += day - 1

        return week_days[total_days % 7]
