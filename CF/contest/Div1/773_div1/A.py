from collections import deque,defaultdict,Counter

t=int(input())
for _ in range(t):
    n,x=[int(x) for  x in input().split()]
    a=[int(x) for  x in input().split()]

    counter=Counter(a)

    ans=0
    for k,_ in sorted(counter.items(),key=lambda x:x[0]):
        if counter[k]>0:
            if counter[k]>counter[k*x]:
                ans+=counter[k]-counter[k*x]
                counter[k*x]=0
            else:
                counter[k*x]-=counter[k]

    print(ans)


