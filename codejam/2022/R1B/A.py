
def maxpan(nums):

    l=0
    r=n-1

    pre=0
    ans=0

    while l<=r:
        if nums[l]<nums[r]:
            if nums[l]>=pre:
                ans+=1
            pre=max(pre,nums[l])
            l += 1


        else:
            if nums[r]>=pre:
                ans+=1
            pre=max(pre,nums[r])
            r -= 1

    return ans


t=int(input())
for i in range(t):
    n=int(input())
    nums=[int(x) for  x in input().split()]
    res=maxpan(nums)
    print('Case #%d: %d'%(i+1,res))

