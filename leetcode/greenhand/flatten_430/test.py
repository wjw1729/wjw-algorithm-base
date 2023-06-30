"""
author:wjw
分析：
"""
class Node:
    def __init__(self,val,pre=None,next=None,child=None):
        self.val=val
        self.pre=pre
        self.next=next
        self.child=child



class Solution:
    def flatten(self, head: 'Node') -> 'Node':

        def dfs(node):
            cur = node
            # 记录链表的最后一个节点
            last = None

            while cur:
                nxt = cur.next
                # 如果有子节点，那么首先处理子节点
                if cur.child:
                    child_last = dfs(cur.child)

                    nxt = cur.next
                    # 将 node 与 child 相连
                    cur.next = cur.child
                    cur.child.prev = cur

                    # 如果 nxt 不为空，就将 last 与 nxt 相连
                    if nxt:
                        child_last.next = nxt
                        nxt.prev  = child_last

                    # 将 child 置为空
                    cur.child = None
                    last = child_last
                else:
                    last = cur
                cur = nxt

            return last

        dfs(head)
        return head


head=Node(1)
head.next=Node(2)
cur=head.next
cur.pre=head
cur.next=Node(3)
cur.next.pre=cur
cur=cur.next

cur.child=Node(7)
childnode=cur.child

cur.next=Node(4)
cur.next.pre=cur

childnode.next=Node(8)
childnode.next.pre=childnode

res=Solution().flatten(head)
print(1)


