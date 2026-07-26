# A088 Min Stack
class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum_stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)

        if not self.minimum_stack:
            self.minimum_stack.append(value)
        else:
            current_minimum = min(value, self.minimum_stack[-1])
            self.minimum_stack.append(current_minimum)

    def pop(self) -> None:
        self.stack.pop()
        self.minimum_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
