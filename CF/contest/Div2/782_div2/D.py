
def reversesortsum(nums):
    total=sum(nums)
    k=total//n
    ans=[0]*n

    b=[0]*n
    lf=n-k
    for i in range(lf,n):
        b[i]=n-1
    for i in range(n-1,-1,-1):
        if lf>i:
            break
        cur=nums[i]-(b[i]-i)
        if cur==i+1:
            ans[i]=1
        elif cur==1:
            ans[i]=0
            lf-=1
            b[lf]=i-1


    return ans


t=int(input())
for _ in range(t):
    n=int(input())
    nums=[int(x) for x in input().split()]
    res=reversesortsum(nums)
    print(' '.join(str(x) for  x in res))
