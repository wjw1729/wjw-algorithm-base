class Robot:

    def __init__(self, width: int, height: int):
        self.pos = 0
        self.width = width
        self.height = height
        self.pls = []
        self.pls += [[i, 0] for i in range(self.width-1)]
        self.pls += [[self.width - 1, i] for i in range(self.height-1)]
        self.pls += [[i, self.height - 1] for i in range(self.width - 1, 0, -1)]
        self.pls += [[0, i] for i in range(self.height - 1, 0, -1)]
        self.l = 2 * (width + height) - 4

    def move(self, num: int) -> None:
        self.pos += num

    def getPos(self):
        return self.pls[self.pos%self.l]

    def getDir(self) -> str:
        tmp = self.pos  % (self.l)
        if 0 <tmp <= self.width-1:
            return 'East'
        elif self.width-1<tmp <= self.width + self.height - 2:
            return 'North'
        elif self.width + self.height - 2 <tmp <= 2 * self.width + self.height - 3:
            return 'West'
        else:
            return 'South'



r=Robot(6,3)
a=sum([17,21,22,34,1,46,35])
r.move(55)
print(r.getPos(),r.getDir())