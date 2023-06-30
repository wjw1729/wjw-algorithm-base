
q=int(input())

for _ in range(q):
    def solve():
        t=input()
        n=int(input())
        d={}
        sls=set()
        for i in range(n):
            s=input()
            d[s]=i
            sls.add(s)

        m=len(t)
        a=[-1]*m

        for i in range(m):
            for j in range(i,m):
                if t[i:j+1] in sls:
                    a[i]=max(a[i],j+1)

        b=a[:]

        for i in range(1,m):
            b[i]=max(b[i],b[i-1])

        i=0
        ans=[]
        while i<m:
            if b[i]<=i:
                print(-1)
                return
            idx=a.index(b[i])
            ans.append((t[idx:b[i]],idx))
            i=b[i]

        print(len(ans))
        for i,j in ans:
            print(d[i]+1,j+1)

    solve()




