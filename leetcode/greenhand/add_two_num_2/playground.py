import json


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
        l3=ListNode(0)
        node3=l3
        while node1 or node2:
            if node1==None:
                node1=ListNode(0)
            if node2==None:
                node2=ListNode(0)
            carry, res = add(node1.val, node2.val, carry)
            node3.next = ListNode(res)
            node1 = node1.next
            node2 = node2.next
            node3 = node3.next
        if carry==1:
            node3.next=ListNode(1)
            node3=node3.next
        node3=l3.next
        return node3

def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

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

#l1='[2,4,3]'
#l2='[5,6,4]'

l1='[9,9,9,9,9,9,9]'
l2='[9,9,9,9]'

s=Solution()
result=s.addTwoNumbers(stringToListNode(l1),stringToListNode(l2))
print(listNodeToString(result))