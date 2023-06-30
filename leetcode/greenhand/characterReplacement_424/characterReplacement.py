"""
author:wjw
分析：滑动窗口+哈希存储counter+最大值。
这个思路需要仔细地分析他的执行过程。
核心是出现过k长度的符合要求的滑动窗口后，区间长度就不会减少，如果有更长的会增加，重新更新。反之则会维持。
时间复杂度：O（n）
"""

from collections import defaultdict


class Solution:
    def characterReplacement(self, s, k):

        left = 0
        counter = defaultdict(int)
        maxcounter = 0

        for right in range(len(s)):
            counter[s[right]] += 1
            if counter[s[right]] > maxcounter:
                maxcounter = counter[s[right]]

            if right - left + 1 - maxcounter > k:
                counter[s[left]] -= 1
                left += 1

        return right - left + 1


s = "ABAB"
k = 2
s = "AABABBA"
k = 1

# s = "BAAA"
# k = 0
res = Solution().characterReplacement(s, k)
print(res)
