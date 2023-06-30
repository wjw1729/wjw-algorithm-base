"""
author:wjw
分析：辅助栈，同步进出当前最小值。
"""


class MinStack:
    def __init__(self):
        self.stack = []
        self.auxiliary_stack = []

    def push(self, val):
        self.stack.append(val)
        if self.auxiliary_stack == []:
            self.auxiliary_stack.append(val)

        elif val < self.auxiliary_stack[-1]:
            self.auxiliary_stack.append(val)
        else:
            self.auxiliary_stack.append(self.auxiliary_stack[-1])

    def pop(self):
        self.auxiliary_stack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.auxiliary_stack[-1]


