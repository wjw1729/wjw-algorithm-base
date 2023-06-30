class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l1 = list()
        self.l2 = list()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.l1.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """

        self.l2[:] = self.l1
        self.l1 = list()
        while len(self.l2) != 1:
            self.l1.append(self.l2.pop(0))

        return self.l2.pop(0)

    def top(self) -> int:
        """
        Get the top element.
        """
        self.l2[:] = self.l1

        while len(self.l2) != 1:
            self.l2.pop(0)

        return self.l2.pop(0)

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.l1) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
obj=MyStack()
obj.push(1)
print(obj.empty())
y=obj.top()
print(obj.empty())
x=obj.pop()
print(obj.empty())
print(1)
