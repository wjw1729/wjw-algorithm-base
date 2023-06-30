"""
author：wjw
分析：
"""


class Solution:
    def getIntersectionNode(self, headA,headB):
        d=set()

        node1=headA
        while node1:
            d.add(node1)
            node1=node1.next

        node2=headB

        while node2:
            if node2 in d:
                return node2
            else:
                node2=node2.next



