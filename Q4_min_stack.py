class MinStack:
    def _init_(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)

        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self):
        val = self.stack.pop()

        if val == self.minStack[-1]:
            self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]


s = MinStack()

s.push(-2)
s.push(0)
s.push(-3)

print(s.getMin())  # -3

s.pop()

print(s.top())     # 0
print(s.getMin())  # -2