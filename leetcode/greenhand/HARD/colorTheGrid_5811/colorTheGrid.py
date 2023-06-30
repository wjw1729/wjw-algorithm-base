"""
author:wjw
分析：状态压缩动态规划.dp[i][mask]表示对第i行涂色为mask下的总方案数。
    状态压缩+动态规划。此处压缩的是同一行所有的颜色状态的取值。为了降低状态的数量，这里选择元素较少的作为一行。
    状态中只有相邻元素取不同色（此处即为不同值）时的状态才是有效的，建立mask-color的字典。
    在上步的基础上建立mask有效相邻的字典，便于搜索某一行为mask的前提下，上一行的合法有效mask的取值。
    然后每行进行动态规划的迭代。
    由于在计算改行的dp[i][mask]会用到dp[i-1][mask_last]的值，所以对于这类相邻行间的状态转移方程，我们可以用两个数组进行滚动迭代。
    最后想要的结果就是dp[n-1]的和。
"""

from collections import defaultdict


class Solution:
    def colorTheGrid(self, m, n):

        valid = {}
        for mask in range(3 ** m):
            color = []
            mm = mask

            for i in range(m):
                color.append(mm % 3)
                mm = mm // 3

            if any(color[i] == color[i + 1] for i in range(m - 1)):
                continue
            valid[mask] = color

        adjacent = defaultdict(list)

        for mask1, color1 in valid.items():
            for mask2, color2 in valid.items():
                if any(color1[i] == color2[i] for i in range(m)):
                    continue
                adjacent[mask1].append(mask2)

        f = [int(mask in valid) for mask in range(3 ** m)]

        for i in range(1, n):
            g = [0] * (3 ** m)
            for mask in range(3 ** m):
                for mask_last in adjacent[mask]:
                    g[mask] += f[mask_last]

            f = g

        return sum(f) % (10 ** 9 + 7)


m = 3
n = 2
res = Solution().colorTheGrid(m, n)
print(res)
