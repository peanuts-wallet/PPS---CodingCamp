# A062 2016년
def solution(a, b):
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month_days = [31, 29, 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31]

    total_days = b - 1

    for month in range(a - 1):
        total_days += month_days[month]

    return days[total_days % 7]

