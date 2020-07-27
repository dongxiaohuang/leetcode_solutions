import math
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.min_stack or self.min_stack[-1] >= node:
            self.min_stack.append(node)

    def pop(self):
        # write code here
        node = self.stack.pop()
        if node == self.min_stack[-1]:
            self.min_stack.pop()
        return node
    def top(self):
        # write code here
        return self.stack[-1]
    def getMin(self):
        # write code here
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()