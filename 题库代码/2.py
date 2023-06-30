"""
wjw算法题库：2.捡西瓜
"""
import time


class binaryindexTree:
    def __init__(self,n):
        self.c=[0]*(n+1)
        self.a=[0]*(n+1)
        self.n=n

    def lowbit(self,x):
        return x & -x

    def update(self,x,val):
        self.a[x]=val

        while x<self.n+1:
            self.c[x]=self.a[x]
            lx=self.lowbit(x)
            for i in range(1,lx):
                if 2**i>=lx:
                    break
                self.c[x]=max(self.c[x],self.c[x-i])
            x+=self.lowbit(x)

    def query(self,l,r):
        res=0
        while r>=l:
            res=max(res,self.a[r])
            r-=1
            while r-self.lowbit(r)>=l:
                r-=self.lowbit(r)
                res=max(self.c[r],res)

        return res


#利用树状数组进行状态转移,f[i]表示的是选取i情况下的最大价值（后缀）
def maxvalue(attr):
    n=len(attr)
    f=[0]*(n)
    f[n-1]=attr[n-1][0]

    binat=binaryindexTree(n)#这里有个小移位，f下标0-n-1对应着bit中1-n

    for i in range(n-2,-1,-1):
        idx=i+attr[i][1]+1
        if idx>=n:
            f[i]=attr[i][0]
        else:
            maxf=binat.query(idx+1,n)
            f[i]=attr[i][0]+maxf

        binat.update(i+1,f[i])

    return max(f)



def maxvaluebf(attr):
    n = len(attr)
    f = [0] * (n)
    f[n - 1] = attr[n - 1][0]



    for i in range(n - 2, -1, -1):
        idx = i + attr[i][1] + 1
        if idx >= n:
            f[i] = attr[i][0]
        else:
            maxf=max(f[idx:])
            f[i]=attr[i][0]+maxf

    return f[0]


"""
如何维护一个数据结构，能够查询idx右边的最大值是个问题logn。
"""
from sortedcontainers import SortedList
def maxvaluesl(attr):
    n = len(attr)
    f = [0] * (n)
    f[n - 1] = attr[n - 1][0]

    sl=SortedList()
    sl.add()
    for i in range(n - 2, -1, -1):
        idx = i + attr[i][1] + 1
        if idx >= n:
            f[i] = attr[i][0]
        else:
            1==1
    return f[0]

#换一种角度进行dp方程
#时间复杂度:O(n)，这里的f[i]表示后缀i-n-1能选出的最大价值（i，可选可不选）
def maxvaluedp(attr):
    n = len(attr)
    f = [0] * (n)
    f[n - 1] = attr[n - 1][0]


    for i in range(n - 2, -1, -1):
        idx = i + attr[i][1] + 1
        f[i]=f[i+1]#核心就是这里的状态转移，这样就导致了f是一个非减的数组（随着转移方向），所以就不用二分找最大值。
        if idx >= n:
            f[i] =max( attr[i][0],f[i])
        else:
            f[i]=max(f[i],attr[i][0]+f[idx])

    return f[0]



attr=[[1,1] for _ in range(50000)]
t1=time.time()
ans1=maxvalue(attr)
print(time.time()-t1)
t2=time.time()
ans2=maxvaluebf(attr)
print(time.time()-t2)
t3=time.time()
ans3=maxvaluedp(attr)
print(time.time()-t3)
print(ans1,ans2,ans3)



