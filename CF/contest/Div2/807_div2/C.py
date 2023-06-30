

import bisect

t=int(input())
for _ in range(t):
    n,c,q=[int(x) for x in input().split()]
    s=list(input())
    lls = [n]
    opls=[]
    for _ in range(c):
        l,r=[int(x) for x in input().split()]
        opls.append((l,r))
        lls.append(lls[-1]+r-l+1)


    for _ in range(q):
        k=int(input())


        while k>n:
            idx = bisect.bisect_left(lls, k)
            k=opls[idx-1][0]+k-lls[idx-1]-1

        ans=s[k-1]
        print(ans)