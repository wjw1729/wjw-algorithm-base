"""

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head, k):

        next_node = head

        temp = []
        i = 0
        while next_node:

            node = next_node
            while len(temp) < k and node != None:
                temp.append(node)
                node = node.next

            if len(temp)<k:
                pre_node.next=temp[0]
                break

            next_node = node

            # print(len(temp))
            pre = temp.pop()
            if i == 0:
                head = pre
            else:
                pre_node.next = pre
            node = pre
            while temp:
                node = temp.pop()
                pre.next = node
                pre = node
                #print(len(temp))
            pre_node = node

            if next_node == None:
                pre_node.next = None

            i += 1

        return head


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


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


ls = [1, 2, 3, 4, 5]
k = 4

head = listToListNode(ls)
res = Solution().reverseKGroup(head, k)
print(listNodeToString(res))
