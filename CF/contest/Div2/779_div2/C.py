

def exist(nums):
    n=len(nums)

    total1=0
    for i in range(n):
        if nums[i]==1:
            total1+=1
        if  nums[i]-nums[i-1]>1:
            return False

    return total1==1


t=int(input())

for _ in range(t):
    _=input()
    nums=[int(x) for x in input().split()]
    if exist(nums):
        print('YES')
    else:
        print('NO')

