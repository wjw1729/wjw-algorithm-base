"""
author:wjw
分析：遍历。
"""


def judges(a, b):
    for s in b:
        if s in a:
            return True
    return False


class Solution:
    def maxLength(self, arr):

        arr.sort(key=lambda x:len(x),reverse=True)
        ans = 0
        n = len(arr)
        for i in range(n):
            alph_set = set()
            if i==1:
                print(1)
            for j in range(i, n):
                if j==1:
                    print(1)
                if len(set(arr[j])) != len(arr[j]):
                    continue
                if len(alph_set) + len(arr[j]) > 26 or judges(alph_set, arr[j]):
                    continue
                for s in arr[j]:
                    alph_set.add(s)

            ans = max(ans, len(alph_set))

        return ans


arr = ["un", "iq", "ue"]
arr = ["abcdefghijklmnopqrstuvwxyz"]
arr = ["yy", "bkhwmpbiisbldzknpm"]
arr=["a", "abc", "d", "de", "def"]
res = Solution().maxLength(arr)
print(res)
