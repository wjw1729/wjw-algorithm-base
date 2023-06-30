
from collections import defaultdict



t=int(input())
for _ in range(t):
    n,k=[int(x) for x  in  input().split()]
    a=[int(x) for x  in  input().split()]

    counter=defaultdict(int)
    for c in a:
        counter[c]+=1

    maxg=-1
    l=-1
    r=-1
    pre=-1
    ans=[-1]
    for k1,v in sorted(counter.items(),key=lambda x:x[0]):
        if v>=k:
            if k1==pre+1:
                pre=k1

            else:
                if pre>0 and l>0 and pre-l>maxg:
                    ans=(l,pre)
                    maxg=pre-l

                l=k1
                pre=k1

    if pre > 0 and l > 0 and pre - l > maxg:
        ans = (l, pre)
        maxg = pre - l

    print(*ans)






