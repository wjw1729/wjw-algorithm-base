


t=int(input())

for _ in range(t):
    n=int(input())
    nums=[int(x) for x in input().split()]
    negnums=sum(x<0 for x  in nums)

    nums=[abs(x) for x in nums]
    for i in range(negnums):
        nums[i]=-nums[i]

    check=True
    for i in range(n-1):
        if nums[i]>nums[i+1]:
            check=False
            break

    if check:
        print('YES')
    else:
        print('NO')


