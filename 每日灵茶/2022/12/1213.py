"""
题干：https://atcoder.jp/contests/arc125/tasks/arc125_c

"""


N,K=[int(x) for  x in input().split()]
a=[int(x) for  x in input().split()]

sa=set(a)
maxa=max(a)

la=[]
for i in range(1,maxa):
    if i not in sa:
        la.append(i)

res=list(range(N,maxa,-1))+a+la[::-1]
print(*res)




