"""
author:wjw
分析：筛除有重复字符的字符串，回溯+剪枝。
"""


def judges(a, b):
    for s in b:
        if s in a:
            return True
    return False


def judgearr(a, b):
    for arrb in b:
        if not judges(arrb, a):
            return False
    return True


class Solution:
    def maxLength(self, arr):
        self.ans = 0
        n = len(arr)
        for i in range(n - 1, -1, -1):
            if len(set(arr[i])) != len(arr[i]):
                arr.pop(i)

        total = set()
        for i in range(len(arr)):
            total = total | set(arr[i])

        def backtrack(alpha_set, arr):

            if self.ans == len(total):
                return

            if judgearr(alpha_set, arr) == True:
                self.ans = max(self.ans, len(alpha_set))

                return

            for i in range(len(arr)):
                if len(arr[i]) != len(set(arr[i])):
                    continue
                if judges(alpha_set, arr[i]):
                    continue

                alpha_set = alpha_set | set(arr[i])
                temp = arr[i]
                arr.pop(i)

                backtrack(alpha_set, arr)

                alpha_set = alpha_set - set(temp)
                arr.insert(i, temp)

        backtrack(set(), arr)
        return self.ans


arr = ["un", "iq", "ue"]

arr = ["abcdefghijklmnopqrstuvwxyz"]

arr = ["yy", "bkhwmpbiisbldzknpm"]

arr = ["a", "abc", "d", "de", "def"]

arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]

arr = ["jnfbyktlrqumowxd", "mvhgcpxnjzrdei"]
"""
"""
arr = ["e", "tpgynpylqbyqjaf", "svkgfmpgftxjjrcxxsog", "bxypbbrlckiolfwpqgsoc", "kwnelumrnnsryjdeppanuqbsu"]
res = Solution().maxLength(arr)
print(res)
