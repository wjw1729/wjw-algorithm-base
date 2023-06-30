"""
author:wjw
分析：
    好像改了并没有变好
"""


def getadjcent(point):
    adj = []
    for i in range(4):
        adj.append(point[:i] + str((int(point[i]) + 1) % 10) + point[i + 1:])
        adj.append(point[:i] + str((int(point[i]) + 9) % 10) + point[i + 1:])
    return adj


class Solution:
    def openLock(self, deadends, target):
        deadends = set(deadends)

        if "0000" in deadends:
            return -1

        if target == "0000":
            return 0

        queue = [("0000", 0)]
        bin = {"0000"}

        while queue:

            point, level = queue.pop(0)

            for next in getadjcent(point):
                if next not in deadends and next not in bin:
                    if next == target:
                        return level + 1
                    queue.append((next, level + 1))
                    bin.add(next)

        return -1


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"



res = Solution().openLock(deadends, target)
print(res)
