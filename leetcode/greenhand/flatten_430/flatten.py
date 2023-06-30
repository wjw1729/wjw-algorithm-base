"""
author:wjw
分析：
"""
class Node:
    def __init__(self,val,prev=None,next=None,child=None):
        self.val=val
        self.prev=prev
        self.next=next
        self.child=child



class Solution:
    def flatten(self, head: 'Node') -> 'Node':

        def dfs(node):

            if node.child:
                childend = dfs(node.child)
                if node.next:
                    childend.next = node.next
                    node.next.prev = childend

                node.next = node.child
                node.child.prev = node
                node.child = None

            if not node.next:
                return node
            return dfs(node.next)

        if not head:
            return head
        dfs(head)
        return head


head=Node(1)
head.next=Node(2)
cur=head.next
cur.prev=head
cur.next=Node(3)
cur.next.prev=cur
cur=cur.next

cur.child=Node(7)
childnode=cur.child

cur.next=Node(4)
cur.next.prev=cur

childnode.next=Node(8)
childnode.next.prev=childnode



head=Node(1)
head.child=Node(2)
cur=head.child
cur.child=Node(3)
res=Solution().flatten(head)
print(1)


