from collections import deque,defaultdict


def minv(a):
    c = defaultdict(int)

    for a0 in a:
        c[a0] += 1

    if len(c)==1:
        return 1


    ans=0
    sig=0
    for i, (k, v) in enumerate(sorted(c.items(), key=lambda x: x[0])):



        if v >= 2:
            ans+=1
        else:
            sig+=1


    return ans+(sig+1)//2



t=int(input())

for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]

    print(minv(a))




