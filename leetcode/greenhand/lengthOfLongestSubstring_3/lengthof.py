"""
author:wjw
分析：维护一个包含最长不重复子串的滑动窗口。维护规则：遇到不重复的就添加，遇到重复的就删除重复字符即以前的部分，接续进行
心得：滑动窗口yyds
"""


class Solution:
    def lengthofLongestSubstring(self, s):
        window = []
        max_length = 0
        for i in range(len(s)):
            if s[i] not in window:
                window.append(s[i])
            else:
                max_length = max(max_length, len(window))
                idx = window.index(s[i])
                window = window[idx + 1:]
                window.append(s[i])
        max_length = max(max_length, len(window))
        return max_length


s = 'dvdf'
result = Solution().lengthofLongestSubstring(s)
print(result)
