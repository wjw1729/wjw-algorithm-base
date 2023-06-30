"""
author:wjw
分析：维护一个滑动窗口内部值的有序列表。
    时间复杂度：O(nlogn)
"""

from sortedcontainers import SortedList
class Solution:
    def longestSubarray(self,nums,limit):
        window=SortedList()
        ans=0
        left=0

        for right in range(len(nums)):
            window.add(nums[right])

            while window[-1]-window[0]>limit:
                window.remove(nums[left])
                left+=1

            ans=max(ans,len(window))
        return ans



