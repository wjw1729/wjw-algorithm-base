"""原约束等价位a[i]^j>a[j]^i
dp

"""

t=int(input())
for _ in range(t):
    n=int(input())
    a=[int(x) for x in input().split()]


    f=[1]

    for i in range(n):
        f.append(1)
        for j in range(i-1,max(0,i-512)-1,-1):
            if a[i]^j>a[j]^i:
                f[i+1]=max(f[i+1],f[j+1]+1)


    print(max(f))

