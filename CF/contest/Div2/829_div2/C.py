
t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x  in input().split()]

    def solve():
        if n%2==1:
            print(-1)
            return
        ans=[]
        for i in range(0,n,2):
            if a[i]==a[i+1]:
                ans.append((i,i+1))

            else:
                ans.append((i,i))
                ans.append((i+1,i+1))

        print(len(ans))
        for x in ans:
            print(x[0]+1,x[1]+1)

    solve()