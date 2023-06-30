

def makeequalwithmod(nums):
    flag=False
    if 0 in nums:
        flag=True

    flag1=False
    if  1 in nums:
        flag1=True

    if flag and flag1:
        return False

    if flag1:
        numset=set(nums)
        for x in nums:
            if x-1 in numset or x+1 in numset:
                return False

    return True


t=int(input())
for _ in range(t):
    _=input()
    nums=[int(x) for x in input().split()]
    if makeequalwithmod(nums):
        print('YES')
    else:
        print('NO')
