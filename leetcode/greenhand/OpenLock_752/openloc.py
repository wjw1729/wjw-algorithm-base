"""
author:wjw
分析：广度优先搜索+迭代
    其实好像可以优化：用距离来优化，并不用遍历所有点，如何在遍历所有点之前判断target已经不可能到了？
"""


class Solution:
    def openLock(self, deadends, target):

        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0

        queue = [("0000", 0)]
        bin = set("0000")
        while queue:
            node, level = queue.pop(0)

            for i in range(4):
                ladjcent = node[:i] + str((int(node[i]) + 9) % 10) + node[i + 1:]
                radjcent = node[:i] + str((int(node[i]) + 1) % 10) + node[i + 1:]
                if ladjcent == target:
                    return level + 1
                if radjcent == target:
                    return level + 1
                if ladjcent not in deadends and ladjcent not in bin:
                    queue.append((ladjcent, level + 1))
                    bin.add(ladjcent)
                if radjcent not in deadends and radjcent not in bin:
                    queue.append((radjcent, level + 1))
                    bin.add(radjcent)

        return -1


deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"

deadends = ["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"]
target = "8888"

res = Solution().openLock(deadends, target)
print(res)
