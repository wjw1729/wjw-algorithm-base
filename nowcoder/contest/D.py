n=int(input())
b=[int(x) for x  in input().split()]


f=[[0]*2 for _ in range(n)]


for i in range(1,n):
    f[i][0]=max(f[i-1][0],f[i-1][1]+abs(1-b[i-1]))
    f[i][1]=max(f[i-1][0]+abs(b[i]-1),f[i-1][1]+abs(b[i]-b[i-1]))

print(max(f[n-1]))


