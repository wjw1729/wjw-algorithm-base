
t=int(input())

for _ in range(t):
    l,r,x=[int(x) for  x in input().split()]
    a,b=[int(x) for  x in input().split()]

    def solve():
        if a==b:
            print(0)
            return
        if (abs(a-l)<x and abs(a-r)<x) or (abs(b-l)<x and abs(b-r)<x):
            print(-1)
            return
        if abs(b-a)>=x:
            print(1)
            return
        if (abs(a-l)>=x and abs(b-l)>=x) or (abs(a-r)>=x and abs(b-r)>=x):
            print(2)
            return

        print(3)
        return

    solve()


