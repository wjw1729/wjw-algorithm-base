
def solve(n,kls):
    n-=kls[5]
    if n<0:
        return False

    n-=kls[4]
    kls[0]-=kls[4]*11

    if kls[3]>0:
        n-=kls[3]
        less=5*kls[3]#2x2个数
        if less<=kls[1]:
            kls[1]-=less
        else:
            kls[0]-=(less-kls[1])*4
            kls[1]=0

    if kls[2]>0:
        n-=kls[2]//4
        less=kls[2]%4
        if less==0:
            pass
        elif less==1:
            n-=1
            if kls[1]>=5:
                kls[1]-=5
                kls[0]-=7
            else:
                kls[0]-=7+(5-kls[1])*4
                kls[1]=0



        elif less==2:
            n-=1
            if kls[1]>=3:
                kls[1]-=3
                kls[0]-=6
            else:
                kls[0] -= 6 + (3 - kls[1]) * 4
                kls[1] = 0

        else:
            n-=1
            if kls[1]>=1:
                kls[1]-=1
                kls[0]-=5
            else:
                kls[0] -= 5 + (1 - kls[1]) * 4
                kls[1] = 0

    if kls[1]>0:
        n-=kls[1]//9
        less=kls[1]%9
        if less==0:
            pass
        else:
            n-=1
            kls[0]-=36-4*less

    if kls[0]>0:
        n-=(kls[0]-1)//36+1

    return n>=0






t=int(input())
for _ in range(t):
    n=int(input())
    kls=[int(x) for  x in input().split()]
    res = solve(n, kls)
    if res:
        print('Yes')
    else:
        print('No')

