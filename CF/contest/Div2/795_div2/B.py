from collections import defaultdict

t=int(input())
for _ in range(t):
    n=int(input())
    s=[int(x) for x  in input().split()]

    sls=defaultdict(list)
    for i in range(n):
        sls[s[i]].append(i)

    check=True
    for k,v in sls.items():
        if len(v)==1:
            check=False
            break
        else:
            sls[k]=[v[-1]]+v[:-1]
    if not check:
        print(-1)
    else:
        ans=[0]*n
        for i in range(n-1,-1,-1):
            ans[i]=sls[s[i]].pop()

        print(*[x+1 for x in ans])
