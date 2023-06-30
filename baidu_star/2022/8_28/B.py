
n=int(input())
s=[0]*n
f=[0]*n
t=[0]*n
for i in range(n):
    s[i],f[i],t[i]=[int(x) for x  in input().split()]


def solve():
    if len(set(t))>1:
        print('N')
        return

    tt=t[0]
    sls=[(s[i]%tt,f[i]%tt) for i in range(n)]

    sls.sort()

    tans=0
    for i in range(1,n):
        if sls[i][0]<=sls[i-1][1]:
            print('N')
            return
        tans+=sls[i][1]-sls[i][]



