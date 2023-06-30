"""
author:wjw
分析：

"""
class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def mergeKLists(self,lists):
        while None in lists:
            lists.remove(None)

        if lists == []:
            return None

        n=len(lists)
        head=lists[0]
        point=0
        for i in range(1,n):
            if lists[i].val<head.val:
                head=lists[i]
                point=i

        lists[point]=lists[point].next
        prenode=head

        if lists[point] == None:
            lists.pop(point)

        while lists:
            node=lists[0]
            point=0
            for i in range(len(lists)):
                if lists[i].val<node.val:
                    node=lists[i]
                    point=i

            prenode.next=node
            prenode=node
            lists[point]=lists[point].next
            if lists[point]==None:
                lists.pop(point)

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

lists = [[1,4,5],[1,3,4],[2,6]]
lists=[[1],[0]]

for i in range(len(lists)):
    lists[i]=listToListNode(lists[i])

res=Solution().mergeKLists(lists)
print(res)