import math

t=int(input())

for _ in range(t):
    n,l,r=[int(x) for x in input().split()]
    a=[0]*n

    for i in range(n-1,-1,-1):
        #st=((l-1)//(i+1)+1)*(i+1)
        st=math.ceil(l/(i+1))*(i+1)
        check=False
        for j in range(st,r+1,i+1):

                a[i]=j
                check=True
                break


        if not check:
            break

    if not check:
        print('NO')
    else:
        print('YES')
        print(*a)
