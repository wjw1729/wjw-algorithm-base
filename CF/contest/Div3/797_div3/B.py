

t=int(input())

for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for x  in input().split()]

    gap=[0]*n
    zero=[False]*n
    for i in range(n):
        gap[i]=a[i]-b[i]
        if b[i]==0:
            zero[i]=True

    nozero=set(gap[i] for i in range(n) if zero[i]==False)
    zeromax=max([gap[i] for i in range(n) if zero[i]]+[0])
    if len(nozero)>1:
        print('NO')
    elif len(nozero)==0:
        print('YES')
    elif list(nozero)[0]<zeromax:
        print('NO')
    else:
        print('YES')






