"""
author:wjw
分析：打家劫舍二叉树版
"""
from collections import defaultdict


class Solution:
    def rob(self, root):

        def midlast(root):
            if root:
                return midlast(root.left) + midlast(root.right) + [root]
            else:
                return []

        midlast_ls = midlast(root)
        f = defaultdict(int)
        g = defaultdict(int)

        for i in range(len(midlast_ls)):
            if midlast_ls[i].left == None and midlast_ls[i].right == None:
                f[midlast_ls[i]] = midlast_ls[i].val
                g[midlast_ls[i]] = 0
                continue
            if midlast_ls[i].right != None:
                f[midlast_ls[i]] = g[midlast_ls[i].right] + midlast_ls[i].val
                g[midlast_ls[i]] = max(f[midlast_ls[i].right], g[midlast_ls[i].right])

            if midlast_ls[i].left != None:
                f[midlast_ls[i]] += g[midlast_ls[i].left]
                g[midlast_ls[i]] += max(f[midlast_ls[i].left], g[midlast_ls[i].left])

        return max(f[root], g[root])
