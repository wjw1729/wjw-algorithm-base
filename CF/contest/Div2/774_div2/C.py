from collections import deque,defaultdict
import bisect

powerls=[2**i for i in range(41) if 2**i<=10**12]

c=6
i=4
while c<=10**12:
    powerls.append(c)
    c*=i
    i+=1

powerls.sort()


t=int(input())
for _ in range(t):
    n=int(input())


    d=defaultdict(set)
    for i,c in enumerate(powerls):
        d[c].add(i)

    def dfs(n):
        if n in d:
            return

        res=float('inf')
        idx=bisect.bisect_right(powerls,n)


        for i in range(idx-1,-1,-1):
            dfs(n-powerls[i])
            if i not in d[n-powerls[i]] and res>len(d[n-powerls[i]])+1:
                res=len(d[n-powerls[i]])+1
                d[n]=d[n-powerls[i]]|{i}

    dfs(n)

    print(len(d[n]))












