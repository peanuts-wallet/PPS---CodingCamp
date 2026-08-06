class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_map = {employee.id: employee for employee in employees}

        def dfs(employee_id):
            employee = employee_map[employee_id]
            return employee.importance + sum(dfs(sub_id) for sub_id in employee.subordinates)

        return dfs(id)