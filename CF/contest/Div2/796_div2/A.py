

t=int(input())
for _ in range(t):
    x=int(input())


    for i in range(31):
        if x &(1<<i):
            l1=i
            break
    if x>(1<<l1):
        print(1<<l1)
    else:
        for i in range(31):
            if x %2==0:
                l0=i
                break

            x>>=1

        ans=(1<<l0)+(1<<l1)
        print(ans)

