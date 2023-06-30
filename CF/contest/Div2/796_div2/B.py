

t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x  in input().split()]

    odd=False
    enum=0

    for i in a:
        if i%2==1:
            odd=True
        else:
            enum+=1


    if odd:
        print(enum)
    else:
        ans=float('inf')
        for i in a:
            if i%2==0:
                tmp=0
                while tmp<ans and i%2==0:
                    i//=2
                    tmp+=1

                ans=min(ans,tmp)



        print(ans+enum-1)

