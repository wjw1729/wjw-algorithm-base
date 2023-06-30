"""
题目:
窗口众数

时间复杂度:O((n-k)klogk).也可以不排序，遍历
"""

from collections import defaultdict
class Solution:
    def windowmode(self,nums,k):
        n=len(nums)
        ans=[]
        counter=defaultdict(int)

        for num in nums[:k]:
            counter[num]+=1

        ans.append(list(sorted(counter.items(),key=lambda x:(-x[1],x[0])))[0][0])


        for i in range(1,n-k+1):
            counter[nums[i-1]]-=1
            counter[nums[i+k-1]]+=1

            ans.append(list(sorted(counter.items(), key=lambda x: (-x[1], x[0])))[0][0])


        return ans


ls=input().strip().split()
n,k=[int(x) for x in ls]
ls=input().strip().split()
ls=[int(x) for x in ls]

print(Solution().windowmode(ls,k))





