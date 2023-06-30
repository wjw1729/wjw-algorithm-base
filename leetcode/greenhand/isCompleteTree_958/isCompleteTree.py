"""
author:wjw
分析：广度优先搜索+编号
"""


class Solution:
    def isCompleteTree(self, root):
        queue = [(root, 1)]
        i = 0

        while i < len(queue):
            node, num = queue[i]

            if node.left != None:
                queue.append((node.left, 2 * num))
            if node.right != None:
                queue.append((node.right, 2 * num + 1))
            i += 1
        return queue[-1][1] == len(queue)
