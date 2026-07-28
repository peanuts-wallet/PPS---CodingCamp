# B002 Employee Importance
from typing import List


"""
# Definition for Employee.
class Employee:
    def __init__(
        self,
        id: int,
        importance: int,
        subordinates: List[int]
    ):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(
        self,
        employees: List['Employee'],
        id: int
    ) -> int:

        employee_map = {}

        for employee in employees:
            employee_map[employee.id] = employee

        total_importance = 0
        stack = [id]

        while stack:
            employee_id = stack.pop()
            employee = employee_map[employee_id]

            total_importance += employee.importance

            for subordinate_id in employee.subordinates:
                stack.append(subordinate_id)

        return total_importance

