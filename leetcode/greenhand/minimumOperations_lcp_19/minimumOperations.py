"""
author:wjw
分析：
"""
class Solution:
    def minimumOperations(self, leaves: str) -> int:
        n = len(leaves)
        dp_r = [0] * n
        dp_ry = [float('inf')] * n
        dp_ryr = [float('inf')] * n

        if leaves[0] == 'r':
            dp_r[0] = 0
        else:
            dp_r[0] = 1
        dp_ry[0] = float('inf')
        """
        if leaves[0:2]==('rr' or 'yy'):
            dp_ry[1]=1
        elif leaves[0:2]='ry':
            dp_ry[1]=0
        else:
            dp_ry[1]=2
        """
        for i in range(1, n):

            if leaves[i] == 'r':
                dp_r[i] = dp_r[i - 1]
                if i >= 1:
                    dp_ry[i] = min(dp_ry[i - 1] + 1, dp_r[i - 1] + 1)
                if i >= 2:
                    dp_ryr[i] = min(dp_ry[i - 1] , dp_ryr[i - 1])
            else:
                dp_r[i] = dp_r[i - 1] + 1
                if i >= 1:
                    dp_ry[i] = min(dp_ry[i - 1], dp_r[i - 1])
                if i >= 2:
                    dp_ryr[i] = min(dp_ryr[i - 1] + 1, dp_ry[i - 1] + 1)

        return dp_ryr[-1]

leaves = "rrryyyrryyyrr"
res=Solution().minimumOperations(leaves)
print(res)