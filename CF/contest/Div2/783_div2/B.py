

def social_distance(nums):

    nums.sort()

    pre=nums[0]
    i=1

    while i<n and pre<=m-1:
        pre+=max(nums[i-1],nums[i])+1
        i+=1

    if i<n:
        return False
    if m-1-pre+nums[0]<nums[-1]:
        return False

    return True





t=int(input())

for _ in range(t):
    n,m=[int(x) for x in input().split()]
    nums=[int(x) for x in input().split()]
    if social_distance(nums):
        print('YES')
    else:
        print('NO')

