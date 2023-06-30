"""
author:wjw
分析：只用一次遍历.一次遍历的方法就是将结点存放到list中，在进行链接的操作即可。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head, left, right):
        vhead = ListNode()
        vhead.next = head
        nodels = []
        node = vhead
        while node:
            nodels.append(node)
            node = node.next

        nodels.append(None)

        nodels[left - 1].next = nodels[right]
        for i in range(right, left, -1):
            nodels[i].next = nodels[i - 1]

        nodels[left].next = nodels[right + 1]

        return vhead.next
