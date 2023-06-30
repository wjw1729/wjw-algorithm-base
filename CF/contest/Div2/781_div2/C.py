


from collections import defaultdict
def maxtimes(parents):

    parents=[0]+parents
    counter=defaultdict(int)

    for i in parents:
        counter[i]+=1


    def solve(nums,days):
        if len(nums)>days:
            return False
        injdays=len(nums)
        nums=[x-1 for x in nums if x>1]
        nums.sort(reverse=True)


        for i,num in enumerate(nums):

            injdays+=max(num+1+i-days,0)#最少需注射的天数

            if injdays>days:
                return False
        return True

    nums=list(counter.values())
    ans=0

    l=0
    r=10**9
    while l<=r:
        mid=(l+r+1)//2
        if solve(nums,mid):
            ans=mid
            r=mid-1
        else:
            l=mid+1


    return ans



t=int(input())

for _ in range(t):
    _=input()
    parents=[int(x) for x in input().split()]
    print(maxtimes(parents))
