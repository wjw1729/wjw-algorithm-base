n,x=[int(x) for x  in input().split()]

f=[0]*(500001)


a=[int(x) for x  in input().split()]

def solve():
    for i in a:
        f[i]+=1


    for i in range(1,x):
        if f[i]%(i+1)==0:
            f[i+1]+=f[i]//(i+1)
            f[i]=0

    for i in range(1,x):
        if f[i]!=0:
            print('No')
            return
    print('Yes')

solve()


