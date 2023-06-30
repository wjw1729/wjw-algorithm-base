
def minadd(a,b):
    if a<b:
        return 0,b
    n=len(str(a))
    m=len(str(b))

    if a//10**(n-m)<b:
        t=n-m
        ans=b*10**t
    elif a//10**(n-m)==b:
        if n==m or a%10**(n-m)==10**(n-m)-1:
            ans=b*10**(n-m+1)
            t=n-m+1
        else:
            ans=a+1
            t=n-m

    else:
        t=n-m+1
        ans=b*10**t

    return t,ans


def minops(nums):

    ans=0
    pre=None
    for num in nums:
        if pre!=None:
            t,num1=minadd(pre,num)
            ans+=t
            pre=num1
        else:
            pre=num

    return ans

t=int(input())
for i in range(t):
    n=int(input())
    nums=[int(x) for x in input().split()]
    res=minops(nums)
    print('Case #%d: %d'%(i+1,res))


