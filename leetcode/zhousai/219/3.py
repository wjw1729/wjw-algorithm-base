"""
author:wjw
分析：得分的差值就是bob移除的石子的和。问题转换为两个人抢石头的问题，都想和最小。
    石子游戏的精髓在于选的人刚好碰到偶数长度的列表时，是有权决定下一个人选择是从奇数位选还是偶数位选择的。
"""

class Solution:
    def stoneGameVII(self,stones):
        n = len(stones)
        dp=[[0]*n for _ in range(n) ]
        sel=[[0]*n for _ in  range(n)]

        

stones=[721,979,690,84,742,873,31,323,819,22,928,866,118,843,169,818,908,832,852,480,763,715,875,629]
res=Solution().stoneGameVII(stones)
print(res)