"""
author:wjw
分析：递归。深度太大，还是会超时。
"""

from functools import lru_cache
class Solution:
    def stoneGameII(self, piles):
        @lru_cache(None)
        def total(start, end, M, turn):
            if end - start + 1 <= 2 * M:
                return sum(piles[start:end + 1]) * turn
            else:
                res = float('-inf') if turn > 0 else float('inf')
                for x in range(1, 2 * M + 1):
                    tmp = sum(piles[start:start + x]) * turn + total(start + x, end, max(M, x), -turn)

                    if turn == 1:
                        res = max(tmp, res)
                    else:
                        res = min(tmp, res)

                return res

        return (sum(piles) + total(0, len(piles) - 1, 1, 1)) // 2


piles = [2, 7, 9, 4, 4]
piles = [3111, 4303, 2722, 2183, 6351, 5227, 8964, 7167, 9286, 6626, 2347, 1465, 5201, 7240, 5463, 8523, 8163, 9391,
         8616, 5063, 7837, 7050, 1246, 9579, 7744, 6932, 7704, 9841, 6163, 4829, 7324, 6006, 4689, 8781, 621]
res = Solution().stoneGameII(piles)
print(res)
