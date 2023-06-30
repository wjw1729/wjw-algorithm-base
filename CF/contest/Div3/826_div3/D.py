import math
t=int(input())

for _ in range(t):
    m=int(input())
    a=[int(x) for x in input().split()]
    n=int(math.log2(m))

    def solve(a):
        ans=0
        for _ in range(n):
            b=[0]*(len(a)//2)
            for i in range(0,len(a),2):
                if int(math.ceil(a[i]/2))!=int(math.ceil(a[i+1]/2)):
                    print(-1)
                    return
                b[i//2]=int(math.ceil(a[i]/2))
                if a[i+1]<a[i]:
                    ans+=1
            a=b[:]



        print(ans)

    solve(a)