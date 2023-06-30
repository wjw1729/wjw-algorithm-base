"""from collections import defaultdict


class Allocator:

    def __init__(self, n: int):
        self.pos = 0
        self.n = n
        self.id = defaultdict(int)
        self.array = [0] * n

    def allocate(self, size: int, mID: int) -> int:

        def get(i):

            res = self.n - i >= size and all(x == 0 for x in self.array[i:i + size])
            if res == True:
                return True, -1
            if self.n - i < size:
                return False, self.n

            for j in range(i + size - 1, -1, -1):
                if self.array[j] != 0:
                    idx = j
                    break

            return res, idx

        check = False
        i = 0

        while not check and i < self.n:
            while i<self.n and self.array[i] != 0:
                i += 1

            tmp = get(i)
            if tmp[0]:
                check = True
                break
            i = tmp[1] + 1
        if not check:
            return -1
        self.array[i:i + size] = [mID] * size
        self.id[mID] += size
        return i

    def free(self, mID: int) -> int:
        ans = self.id[mID]
        for i in range(self.n):
            if self.array[i] == mID:
                self.array[i] = 0
        self.id[mID]=0
        return ans"""

from collections import defaultdict

class Allocator:

    def __init__(self, n: int):
        self.ids = defaultdict(int)
        self.array = [0] * n
        self.n = n

    def allocate(self, size: int, mID: int) -> int:

        def get(i):
            if self.n - i < size:
                return False, -1

            check = True
            for ii in range(i, i + size):
                if self.array[ii] != 0:
                    tag = ii
                    check = False
            if check:
                return True, -1
            return False, tag

        i = 0
        while i < self.n:
            print(i)

            while i < self.n and self.array[i] != 0:
                i += 1

            tmp = get(i)
            if tmp[0]:
                self.array[i:i + size] = [mID] * size
                self.ids[mID] += size
                return i
            else:
                if tmp[1]==-1:
                    b
                i = tmp[1] + 1

        return -1

    def free(self, mID: int) -> int:

        ans = self.ids[mID]
        self.ids[mID] = 0

        for i in range(self.n):
            if self.array[i] == mID:
                self.array[i] = 0

        return ans




"""print(al.allocate(1, 1))
print(al.allocate(1, 2))
print(al.allocate(1, 3))
print(al.free(2))
print(al.allocate(3, 4))
print(al.allocate(1, 1))
print(al.allocate(1, 1))
print(al.free(1))
print(al.allocate(10, 2))
print(al.free(7))"""
pls=["Allocator","free","allocate","allocate","allocate","allocate","free","allocate","free"]
qls=[[5],[4],[9,5],[5,8],[4,8],[3,2],[6],[9,9],[6]]
pls=["Allocator","allocate","allocate","allocate","allocate","free","free","free","allocate","allocate","allocate","allocate","free","free","free","free","free","free","free","allocate","free","free","allocate","free","allocate","allocate","free","free","free","allocate","allocate","allocate","allocate","free","allocate","free","free","allocate","allocate","allocate","allocate","allocate","allocate","allocate","free","free","free","free"]
qls=[[50],[12,6],[28,16],[17,23],[50,23],[6],[10],[10],[16,8],[17,41],[44,27],[12,45],[33],[8],[16],[23],[23],[23],[29],[38,32],[29],[6],[40,11],[16],[22,33],[27,5],[3],[10],[29],[16,14],[46,47],[48,9],[36,17],[33],[14,24],[16],[8],[2,50],[31,36],[17,45],[46,31],[2,6],[16,2],[39,30],[33],[45],[30],[27]]
pls=["Allocator","allocate","allocate","allocate","free","allocate","allocate","allocate","free","allocate","free"]
qls=[[10],[1,1],[1,2],[1,3],[2],[3,4],[1,1],[1,1],[1],[10,2],[7]]


al = Allocator(qls[0][0])
for x,y in zip(pls[1:],qls[1:]):
    if x=='free':
        res=al.free(y[0])
        print(res)
        if res==28:
            1==1
    else:
        res=al.allocate(y[0],y[1])
        print(res)
        if res==28:
            1==1


