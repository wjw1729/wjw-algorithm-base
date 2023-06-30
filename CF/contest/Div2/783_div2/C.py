
def makeitin(nums):

    ans=float('inf')
    for i in range(n):
        cnt=0

        t=0
        for j in range(i-1,-1,-1):
            t=t*nums[j+1]//nums[j]+1
            cnt+=t
        t=0
        for j in range(i+1,n):
            t=t*nums[j-1]//nums[j]+1
            cnt+=t
        ans=min(cnt,ans)

    return ans



n=int(input())
nums=[int(x) for x in input().split()]
print(makeitin(nums))

