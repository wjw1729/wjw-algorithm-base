from collections import defaultdict,Counter

def solve(a,b):
    for i in range(n):
        while a[i]%2==0:
            a[i]//=2

    for i in range(n):
        while b[i]%2==0:
            b[i]//=2


    a=Counter(a)



    cnt=defaultdict(set)



    for i in range(n-1,-1,-1):

        while b[i]>0 :
            if b[i] in a:
                cnt[b[i]].add(i)
            b[i]//=2



    chs=set()
    for k,v in sorted(a.items(),key=lambda x:-x[0]):
        chse=cnt[k]-chs
        if len(chse)<v:
            return False
        for j in list(chse)[:v]:
            chs.add(j)

    return True



t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x in input().split()]
    if solve(a,b):
        print('YES')
    else:
        print('NO')



