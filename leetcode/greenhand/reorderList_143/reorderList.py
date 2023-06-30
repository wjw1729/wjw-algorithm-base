"""
author:wjw
分析：重排链表，将链表遍历，每个结点存放到list中，然后依次从前往后取结点，同时从list中pop()，拼接即可。用total记录链表长度，便于终止。
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head):
        nodels = []
        total = 0
        node = head
        while node:
            nodels.append(node)
            node = node.next
            total += 1

        vhead = ListNode()
        node = vhead
        while total > 0:
            node.next = head

            nextnode = head.next
            head.next = nodels.pop()

            node = head.next
            head = nextnode
            total -= 2

        node.next = None
        return vhead.next


def list2listNode(lista):
    head = ListNode()
    node = head
    for num in lista:
        node.next = ListNode(num)
        node = node.next

    return head.next


def listnode2list(listnodea):
    ans = []
    while listnodea:
        ans.append(listnodea.val)
        listnodea = listnodea.next

    return ans


lista = [1, 2, 3, 4, 5, 6]
res = Solution().reorderList(list2listNode(lista))
print(listnode2list(res))
