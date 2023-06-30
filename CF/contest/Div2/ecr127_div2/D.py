def minimalscore(nums,x):

    total=0
    for i in range(1,n):
        total+=abs(nums[i]-nums[i-1])

    minx=min(nums)
    maxx=max(nums)

    if minx>1:
        total+=min(2*(minx-1),nums[0]-1,nums[-1]-1)

    if maxx<x:
        total+=min(2*(x-maxx),x-nums[0],x-nums[-1])


    return total






t=int(input())
for _ in range(t):
    n,x=[int(x) for x in input().split()]
    nums=[int(x) for  x in input().split()]
    print(minimalscore(nums,x))