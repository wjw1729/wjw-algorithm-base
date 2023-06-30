


t=int(input())
for _ in range(t):
    n=int(input())
    nums=[int(x) for x in input().split()]
    ans=0
    check=True
    for i in range(n-2,-1,-1):
        if nums[i+1]==0:
            check=False
            break
        while nums[i]>=nums[i+1]:
            nums[i]//=2
            ans+=1
    if check:
        print(ans)
    else:
        print(-1)

