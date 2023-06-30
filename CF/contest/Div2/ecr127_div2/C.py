def mostcanbuy(nums,x):
    nums.sort()
    ans=0

    presum=[0]*(n+1)

    for i in range(1,n+1):
        presum[i]=presum[i-1]+nums[i-1]

    pre=None
    check=True
    for k in range(1,n+1):
        if presum[k]>x:
            check=False
            break
        m=(x-presum[k])//k
        if pre:
            ans+=(pre-m)*(k-1)

        pre=m
    if not check:
        k-=1
    if pre!=None:
        ans+=(pre+1)*k

    return ans

t=int(input())
for _ in range(t):
    n,x=[int(x) for x  in input().split()]
    nums=[int(x) for x in input().split()]
    print(mostcanbuy(nums,x))

