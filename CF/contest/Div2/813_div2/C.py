
t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for  x in input().split()]

    def solve():
        ans=0
        pre=a[-1]
        vis=set()
        idxmap={}
        for i,c in enumerate(a):
            idxmap[c]=i

        midx=-1
        for i in range(n-2,-1,-1):
            if a[i] in vis:
                continue
            if a[i]>pre:
                pre=0
                midx=max(midx,idxmap[a[i]])
            else:
                pre=min(pre,a[i])

        print(len(set(a[:midx+1])))


        return
    solve()




