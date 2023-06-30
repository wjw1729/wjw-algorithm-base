"""
author:wjw
分析：将原list按照奇偶性分为两堆，则每次选择时，先选择的人有权利选择奇堆或者偶堆，而后选择的人只能在剩下的一堆中进行选择。所以对预先分好的两堆，先选择每次选择总和大的那堆中的数就行了。
    同类题：预测赢家486
"""


class Solution:
    def stoneGame(self, piles):
        return True
