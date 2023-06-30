"""
author:wjw
分析：用最小堆来维护。最大堆中不能存放结点，所以我们改为链表的编号信息，随着链表的合并，lists中的链表也不断向后遍历。
    对于链表类题目，如果需要找起头的结点，那么最好自己先创建个head=ListNode，然后它正常，最后返回head.next即可。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import heapq


class Solution:
    def mergeKLists(self, lists):

        head = ListNode()
        prenode = head
        heap = []
        for i in range(len(lists)):
            if lists[i] != None:
                heapq.heappush(heap, (lists[i].val, i))

        while heap:
            _, node_index = heapq.heappop(heap)
            prenode.next = lists[node_index]
            prenode = lists[node_index]
            lists[node_index] = lists[node_index].next
            if lists[node_index] != None:
                heapq.heappush(heap, (lists[node_index].val, node_index))

        return head.next


def listToListNode(numbers):
    # Generate list from the input

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]

for i in range(len(lists)):
    lists[i] = listToListNode(lists[i])

res = Solution().mergeKLists(lists)
print(res)
