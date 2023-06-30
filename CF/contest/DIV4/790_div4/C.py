
def minop(sls):

    ans=float('inf')
    for i in range(26):
        tmp=0
        for j in range(2):
            tmp+=abs(ord(sls[j])-ord('a')-i)

        ans=min(ans,tmp)

    return ans






t=int(input())

for _ in range(t):
    n,m=[int(x) for x in input().split()]
    sls=[]
    for i in range(n):
        sls.append(input())

    res=float('inf')
    for i in range(n):
        for j in range(i+1,n):
            tmp=0
            for k in range(m):
                tmp+=minop([sls[i][k],sls[j][k]])
            res=min(res,tmp)
    print(res)