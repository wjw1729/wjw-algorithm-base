

t=int(input())


for _ in range(t):
    n,b,x,y=[int(x) for x in input().split()]

    nums=[0]*(n+1)
    for i in range(1,n+1):
        if nums[i-1]+x<=b:
            nums[i]=nums[i-1]+x
        else:
            nums[i]=nums[i-1]-y

    print(sum(nums))

