

def mincost(nums):


    presum=[0]*(n+1)
    for i in range(1,n+1):
        presum[i]=presum[i-1]+nums[i-1]

    ans = b *presum[n]
    for i in range(n):
        tmp=b*nums[i]+a*nums[i]+b*(presum[n]-presum[i+1])-(n-i-1)*b*nums[i]
        ans=min(ans,tmp)


    return ans



t=int(input())
for _ in range(t):
    n,a,b=[int(x) for x in input().split()]
    nums=[int(x) for x in input().split()]
    print(mincost(nums))

