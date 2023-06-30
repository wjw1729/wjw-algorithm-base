"""
author：rank+wjw
分析：直接用列表生成式
"""


class Solution:
    def permutation(self, s):
        ans = ['']
        for c in s:
            ans = [word[:k] + c + word[k:] for word in ans for k in range(len(ans[0]) + 1)]

        return list(set(ans))


s = 'aab'
res = Solution().permutation(s)
print(res)
