"""
author:wjw
分析：列表生成式
"""

class Solution:
    def permutation(self,s):
        ans = ['']
        for c in s:
            # This is the most brilliant way!
            ans = [word[:i] + c + word[i:] for word in ans for i in range((word + c).index(c) + 1)]
        return ans



a='abc'
res=Solution().permutation(a)
print(res)