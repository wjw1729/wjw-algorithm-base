def mincells(s):

    presum=[0]*(n+1)
    for i in range(n+1):
        presum[i]=presum[i-1]+int(s[i-1]=='B')

    ans=k
    for i in range(k,n+1):
        ans=min(ans,k-(presum[i]-presum[i-k]))

    return ans



t=int(input())

for _ in range(t):
    n,k=[int(x) for x in input().split()]
    s=input()
    res=mincells(s)
    print(res)