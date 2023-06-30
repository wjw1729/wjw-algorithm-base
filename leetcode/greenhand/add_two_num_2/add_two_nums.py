"""
author:wjw
分析：简简单单的进位加法器，只是如何构建ListNode这一数据结构有点麻烦，可以参考stringtolistnode函数
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def add(num1, num2, carry):
            carry, res = (num1 + num2 + carry) // 10, (num1 + num2 + carry) % 10
            return carry, res

        node1 = l1
        node2 = l2
        carry = 0
        l3 = ListNode
        node3 = l3
        while node1 or node2:
            carry, res = add(node1, node2, carry)
            node3.val = res
            node1 = node1.next
            node2 = node2.next
            node3 = node3.next
            return l3


