"""
author:wjw
分析：双端队列，存储数据为nums的index（是index递增，但nums[index]递减的，位于k区间内）
"""
import collections
class Solution:
    def maxSlidingWindow(self,nums,k):
        n=len(nums)

        q=collections.deque()
        for i in range(k):

            while q and nums[i]>nums[q[-1]]:#注意是while，因为nums[i]可能比前面的都大
                q.pop()
            q.append(i)

        ans=[nums[q[0]]]
        for i in range(k,n):
            while q and nums[i]>nums[q[-1]]:#同上
                q.pop()
            q.append(i)
            if q[0]<=i-k:
                q.popleft()

            ans.append(nums[q[0]])
        return ans


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
res = Solution().maxSlidingWindow(nums, k)
print(res)