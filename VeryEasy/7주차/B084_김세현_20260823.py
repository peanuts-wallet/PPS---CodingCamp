# Big Countries
# LeetCode 595
# SQL 문제이므로 아래 문자열이 제출할 SQL 정답입니다.

sql = """
SELECT name, population, area
FROM World
WHERE area >= 3000000
   OR population >= 25000000;
""".strip()

print(sql)
