# Combine Two Tables
# LeetCode 175
# SQL 문제이므로 아래 문자열이 제출할 SQL 정답입니다.

sql = """
SELECT p.firstName,
       p.lastName,
       a.city,
       a.state
FROM Person AS p
LEFT JOIN Address AS a
    ON p.personId = a.personId;
""".strip()

print(sql)
