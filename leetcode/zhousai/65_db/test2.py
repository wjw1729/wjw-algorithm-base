
class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head) :

        node = head
        headlist = []
        taillist = []
        lens = []

        k = 1
        i = 0
        while node:
            headlist.append(node)
            check = False
            if i == k - 1 or (i < k and node and node.next == None):
                taillist.append(node)
                print(node.val)
                tmptail = node
                check = True

            while i < k and node:
                node = node.next
                i += 1
                if not check and i == k - 1 or (i < k and node and node.next == None):
                    taillist.append(node)
                    print(node.val)
                    tmptail = node
                    check = True

            tmptail.next = None

            lens.append(i)

            i = 0
            k += 1

        def reversenl(head, tail):
            nodelist = []

            while head:
                nodelist.append(head)
                head = head.next

            n = len(nodelist)
            for i in range(n - 1, 0, -1):
                nodelist[i].next = nodelist[i - 1]

            nodelist[0].next = None
            return (nodelist[-1], nodelist[0])

        for i in range(len(headlist)):
            if lens[i] % 2 == 0:
                tmphead, tmptail = reversenl(headlist[i], taillist[i])
                headlist[i] = tmphead
                taillist[i] = tmptail

        for i in range(len(headlist) - 1):
            taillist[i].next = headlist[i + 1]

        return headlist[0]


head=ListNode(0)
head.next=ListNode(4)
head.next.next=ListNode(2)
head.next.next.next=ListNode(1)
head.next.next.next.next=ListNode(3)


res=Solution().reverseEvenLengthGroups(head)
print(res)