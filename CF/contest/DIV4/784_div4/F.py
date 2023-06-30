


def eatingcandies(nums):


    i=0
    j=n-1
    pre=nums[0]
    suf=nums[n-1]
    ans=0
    while i<j:

        if pre<suf:
            i+=1
            pre+=nums[i]
        elif pre>suf:
            j-=1
            suf+=nums[j]
        else:
            ans=n-(j-i-1)
            i+=1
            pre+=nums[i]
            j-=1
            suf+=nums[j]

    return ans

t=int(input())

for _ in range(t):
    n=int(input())
    nums=[int(x) for x  in input().split()]
    print(eatingcandies(nums))






