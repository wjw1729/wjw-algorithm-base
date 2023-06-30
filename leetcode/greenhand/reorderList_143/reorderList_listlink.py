"""
author:wjw
分析：直接用列表存起来，然后做连线操作即可。
"""


class Solution:
    def reorderList(self, head):
        nodels = []
        while head:
            nodels.append(head)
            head = head.next

        n = len(nodels)
        for i in range(n // 2):
            nodels[i].next = nodels[n - 1 - i]
            nodels[n - 1 - i].next = nodels[i + 1]

        nodels[n // 2].next = None
