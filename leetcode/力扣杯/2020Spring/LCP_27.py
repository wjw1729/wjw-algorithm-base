# direction=-1关于m对称。如果对称点等于本身表示不合法。
# direction=1关于0对称。
class BlackBox:

    def __init__(self, n: int, m: int):
        self.states = [0] * (2 * m + 2 * n)  # 0表示关闭，1表示打开
        self.length = 2 * m + 2 * n
        self.d_minus = 2 * m

    def open(self, index: int, direction: int) -> int:
        self.states[index] = 1
        first = True
        nxt = index
        while True:
            if not first and self.states[nxt] == 1:
                break

            if direction == 1:
                nxt = (2 * self.length - nxt) % (self.length)
                direction = -1

            elif direction == -1:
                nxt = (self.d_minus - nxt + self.length) % (self.length)
                direction = 1

            first = False
        return nxt

    def close(self, index: int) -> None:
        self.states[index] = 0


obj = BlackBox(2, 3)
print(obj.open(6, -1))
print(obj.open(4, -1))
print(obj.open(0, -1))
"""
print(obj.close(6))
print(obj.open(0,-1))
"""
