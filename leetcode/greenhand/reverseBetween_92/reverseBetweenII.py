"""
author:wjw
分析：保存反转部分前一个结点，和后一个结点，反转之后连起来即可！
"""

class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next

class Solution:
    def reverseBetween(self,head,left,right):
        vhead=ListNode
        vhead.next=head
        node=vhead
        i=0
        afternode=None

        while node:
            if i==left-1:
                prenode=node
            if i==right+1:
                afternode=node

            node=node.next


        pre=afternode
        node=prenode.next
        time=0
        while time<right-left+1:
            tmp=node.next
            node.next=pre
            pre=node
            node=tmp
            i+=1

        prenode.next=pre

        return vhead.next

