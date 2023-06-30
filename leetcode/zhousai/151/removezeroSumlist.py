"""
author；wjw
分析：1.滑动窗口肯定是不行的，因为只知道如何添加，不知道如何删除，如果要采用这种方法只能固定窗口左端，这就需要维护n个滑动窗，太耗费资源了。
    2.前缀和，遇到list的窗口和的问题，可以首先想到前缀和。用S[i]表示数组长度为i时的前缀和，当存在两个相等的S[i]时，这二者之间的数和为0.

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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


class Solution:
    def removeZeroSumSublists(self, head):
        S = [0]
        ans = 0
        node = head

        while node:
            ans += node.val
            S.append(ans)
            node = node.next

        dete = []
        left = 0

        while left < len(S) - 1:
            isequal=False
            for right in range(left + 1, len(S)):
                if S[left] == S[right]:
                    dete.append([left, right])
                    left = right
                    isequal=True
                    break
            if isequal!=True:
                left += 1
        stablehead=None
        for i in reversed(range(len(dete))):
            left, right = dete[i][0], dete[i][1]
            print(left, right)
            head_node = ListNode(0)
            head_node.next = head
            stablehead = head_node
            for j in range(right):
                if j == left:
                    node1 = head_node
                    print(node1.val)

                head_node = head_node.next
            head_node=head_node.next
            node2 = head_node

            #print(node2.val)
            node1.next = node2
        if not stablehead:
            return head
        return stablehead.next


l1 = [1, 2, -3, 3, 1]
#l1 = [1, 2, 3, -3, 4]
#l1 = [1, 2, 3, -3, -2]
#l1=[1]
l1=[1,2,-2,3,-3,4,-4,5,6]
head = stringToListNode(l1)
res = Solution().removeZeroSumSublists(head)
res = listNodeToString(res)
print(res)
