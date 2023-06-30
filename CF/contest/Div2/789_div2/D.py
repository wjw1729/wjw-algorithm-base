def goods(s):
    cols=[0]*(n*m)
    rows=[0]*(n*m)

    fc=[0]*m
    pre=None
    for i in range(n*m):
        if fc[i % m] == 0 and s[i]=='1':
            cols[i] = cols[i - 1] + 1
        else:
            cols[i] = cols[i - 1]

        if s[i]=='1':
            fc[i%m]+=1
            pre=i

        if pre!=None and i-m<pre:
            rows[i]=rows[i-m]+1
        else:
            rows[i] = rows[i-m]


    return [cols[i]+rows[i] for i in range(n*m)]


t=int(input())

for _ in range(t):
    n,m=[int(x) for x in input().split()]
    s=input()

    res=goods(s)
    print(*res)