import math

def mincost(nums):

    res1=float('inf')
    for i in range(2,n):
        res1=min(res1,(nums[i]+nums[i-2]+1)//2)

    res2=float('inf')
    for i in range(1,n):
        tmp=0
        x=nums[i]
        y=nums[i-1]

        if x<y:
            x,y=y,x
        if x-2*y>0:
            res2=min(res2,(x+1)//2)
            continue

        tmp+=x-y
        tmp+=(4*y-2*x+2)//3
        res2=min(res2,tmp)



    res4=float('inf')

    min1=float('inf')
    min2=float('inf')
    for c in nums:
        if c<min1:
            min2=min1
            min1=c
        elif c<min2:
            min2=c

    res4=min(res4,math.ceil(min1/2)+math.ceil(min2/2))

    return min(res1,res2,res4)




n=int(input())
nums=[int(x) for x in input().split()]
print(mincost(nums))

