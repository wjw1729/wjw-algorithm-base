
n=int(input())

nums=[int(x) for x in input().split()]

def solve():
    for i in range(n-2,-1,-1):
        if nums[i]>nums[i+1]:
            for j in range(n-1,i,-1):
                if nums[j]<nums[i]:
                    nums[i],nums[j]=nums[j],nums[i]

                    nums[i+1:]=nums[i+1:][::-1]

                    print(*nums)
                    return
    print('ERROR')
    return

solve()


