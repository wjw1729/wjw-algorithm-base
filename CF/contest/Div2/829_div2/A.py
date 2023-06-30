
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()

    def solve():
        cnt=0
        for x in s:
            if x=='Q':
                if cnt>0:
                    cnt=0
                cnt-=1

            else:
                cnt+=1
        if cnt<0:
            print('No')
        else:
            print('Yes')

    solve()

