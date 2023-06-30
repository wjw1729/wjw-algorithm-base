

def minops(nums):

    l=None
    for i in range(n-1):
        if nums[i]==nums[i+1]:
            if l==None:
                l=i
            r=i

    if l==None or  r==l:
        return 0

    return max(1,r-l-1)




t=int(input())
for _ in range(t):
    n=int(input())
    nums=[int(x) for x in input().split()]
    print(minops(nums))
