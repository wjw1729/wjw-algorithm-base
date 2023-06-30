class binaryindextree:
    def __init__(self,n):
        self.n=n
        self.c=[0]*(1+n)

    def lowbit(self,x):
        return x&-x

    def update(self,x,val):

        while x<self.n+1:
            self.c[x]+=val
            x+=self.lowbit(x)

    def query(self,x):
        res=0
        while x>0:
            res+=self.c[x]
            x-=self.lowbit(x)

        return res

t=int(input())

for _ in range(t):
    n=int(input())
    nums=[int(x) for x in input().split()]

    nums=nums[::-1]
    bint = binaryindextree(n)

    ans=0
    for i in range(n):
        ans+= bint.query(nums[i])
        bint.update(nums[i], 1)

    print(ans)


