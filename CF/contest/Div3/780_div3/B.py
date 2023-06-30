

def caneatall(nums):

    maxnum=0
    num2=0
    for num in nums:
        if num>maxnum:
            num2 = maxnum
            maxnum=num
        elif num>num2:
            num2=num

    return maxnum<=num2+1


t=int(input())
for _ in range(t):
    _=input()
    nums=[int(x) for x in input().split()]
    if caneatall(nums):
        print('YES')
    else:
        print('NO')

