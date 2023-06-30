
t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]

    t=sum(a)
    if t%2==0:
        print(0)
    else:
        ans=float('inf')
        for x in a:
            if x%2==1:
                tmp=0
                while x%2==1:
                    x//=2
                    tmp+=1

                ans=min(ans,tmp)
            else:
                tmp=0
                while x%2==0:
                    x//=2
                    tmp+=1
                ans=min(ans,tmp)



        print(ans)

