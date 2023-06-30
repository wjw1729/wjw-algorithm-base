
t=int(input())

for _ in range(t):
    n=int(input())
    c=[int(x) for x in input().split()]

    r=[0]*n
    index=[[] for _ in range(n+1)]

    for i,cc in enumerate(c):
        index[cc].append(i)

    for i in range(n):
        res=0
        pre=-1
        for ii in index[i+1]:
            if pre>=0:
                if ii%2!=pre:
                    res+=1
                    pre=ii%2
            else:
                res+=1
                pre=ii%2

        r[i]=res

    print(*r)