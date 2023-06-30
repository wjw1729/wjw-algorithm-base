

t=int(input())

for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]
    b=[int(x) for  x in input().split()]

    def solve():
        cnt1=a.count(1)
        cnt2=b.count(1)

        if cnt1==cnt2:
            if a==b:
                print(0)
                return
            else:
                print(1)
        else:
            cnt=min(cnt1,cnt2)
            c=0
            for i in range(n):
                if a[i]==b[i]==1:
                    c+=1
            if c==cnt:
                print(max(cnt1,cnt2)-c)
            else:
                print(max(cnt1,cnt2)-cnt+1)

    solve()

