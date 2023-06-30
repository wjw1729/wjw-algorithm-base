"""
author:wjw
分析：链表的插入问题，比较容易，麻烦的是要找到三个链接的结点,好像该方法空寂复杂度低，时间复杂度较高
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeInBetween(self, list1, a, b, list2):

        l1=list1
        for i in range(b):
            if i == a-1 :
                l1node = l1
            l1 = l1.next
        l2node = l1.next

        l1node.next = list2  # l1和l2的连接

        l2 = list2

        while l2.next != None:
            l2 = l2.next
        l2.next = l2node

        return list1


def stringToListNode(numbers):
    # Generate list from the input

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


list1 = [0, 1, 2, 3, 4, 5]
a = 3
b = 4
list2 = [1000000, 1000001, 1000002]

list1 = [0,1,2,3,4,5,6]
a = 2
b = 5
list2 = [1000000,1000001,1000002,1000003,1000004]

l1 = stringToListNode(list1)
l2 = stringToListNode(list2)

result = Solution().mergeInBetween(l1, a, b, l2)

result = listNodeToString(result)
print(result)
