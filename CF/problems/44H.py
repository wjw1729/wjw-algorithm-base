

a=[int(x) for x  in list(input())]
n=len(a)
f=[[0]*10 for _ in range(n)]

check=all(a[i+1]-1<=a[i]<=a[i+1]+1 for i in range(n-2,-1,-1))

for j in range(10):
    f[0][j]=1

for i in range(1,n):
    for j in range(10):
            f[i][j]+=sum(f[i-1][k] for k in [2*j-1-a[i],2*j-a[i],2*j+1-a[i]] if 0<=k<=9)

print(sum(f[n-1])-int(check))
