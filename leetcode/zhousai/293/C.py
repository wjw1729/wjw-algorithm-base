from sortedcontainers import SortedDict


class CountIntervals:

    def __init__(self):
        self.d = SortedDict()

    def add(self, left: int, right: int) -> None:
        l, r = left, right
        if l not in self.d:
            self.d[l] = 1
        else:
            self.d[l]+=1
            if self.d[l] ==0:
                del self.d[l]

        if r+1 not in self.d:
            self.d[r + 1] = -1
        else:
            self.d[r+1]-=1
            if self.d[r + 1] == 0:
                del self.d[r + 1]

    def count(self) -> int:
        ans = 0
        t = 0

        for k, v in self.d.items():
            if t==0:
                pre=k
            t += v

            if t==0:
                ans+=k-pre

        return ans

obj=CountIntervals()
#res=obj.count()
#print(res)
obj.add(24,46)
res=obj.count()
print(res)
obj.add(30,35)
res=obj.count()
print(res)
obj.add(6,46)
res=obj.count()
print(res)

