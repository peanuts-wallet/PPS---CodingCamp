# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: list[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: list['Employee'], id: int) -> int:
        employee_map = {}
        
        for employee in employees:
            employee_map[employee.id] = employee
        
        def dfs(employee_id):
            employee = employee_map[employee_id]
            total = employee.importance
            
            for sub_id in employee.subordinates:
                total += dfs(sub_id)
            
            return total
        
        return dfs(id)