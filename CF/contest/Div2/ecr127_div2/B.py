def canconsect(nums):

    total=0
    for i in range(1,n):
        total+=nums[i]-nums[i-1]

    if total>n-1+2:
        return False

    return True




t=int(input())
for _ in range(t):
    n=int(input())
    nums=[int(x) for x in input().split()]
    if canconsect(nums):
        print('YES')
    else:
        print('NO')