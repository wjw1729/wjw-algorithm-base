"""
author:wjw
分析：首先问题可以简化为分为target个街区。

"""


def zone_judge(house):
    if max(house) == min(house) == 0:
        return 1
    ans = 0
    pre = 0
    for i in range(len(house)):
        now = house[i]
        if now != 0 and now != pre:
            ans += 1
        pre = now

    return ans


class Solution:
    def minCost(self, houses, cost, m: int, n, target: int) -> int:
        if zone_judge(houses) > target:
            return -1

        return house


house = [3, 1, 2, 3]
house = [0, 0, 0, 0]
res = zone_judge(house)
print(res)
