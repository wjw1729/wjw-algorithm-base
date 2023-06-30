"""
author:wjw
分析：好题
"""

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        rm_len = len(removable)
        n = len(s)
        m = len(p)

        def isASubsequence(k):

            removeset = set(removable[:k])

            p1 = 0
            p2 = 0
            while p1 < n:
                if p1 not in removeset:
                    if s[p1] == p[p2]:
                        p2 += 1

                if p2 == m:
                    return True
                p1 += 1

            return False

        left = 0
        right = rm_len

        while left <= right:
            mid = (left + right + 1) // 2

            if isASubsequence(mid):
                left = mid + 1
                ans = mid
            else:
                right = mid - 1

        return ans