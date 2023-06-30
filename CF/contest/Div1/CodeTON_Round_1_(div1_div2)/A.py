
def GoodPairs(nums):
    l=nums.index(min(nums))
    r=nums.index(max(nums))

    return l+1,r+1


t=int(input())

for _ in range(t):
    _=input()
    nums=[int(x) for x in input().split()]
    print(' '.join(str(x) for x in GoodPairs(nums)))



