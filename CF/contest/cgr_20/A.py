

def canwin(nums):
    ans=sum(x-1 for x in nums)
    return ans%2==1



t=int(input())

for _ in range(t):
    n=int(input())
    nums=[int(x) for x in input().split()]
    if canwin(nums):
        print('errorgorn')
    else:
        print('maomao90')