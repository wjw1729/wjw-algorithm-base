"""
author:wjw
分析：双向链表+哈希表
"""
class DLinkedNode:
    def __init__(self,key=0,value=0,pre=None,next=None):
        self.key=key
        self.val=value
        self.pre=pre
        self.next=next

class LRUCache:
    def __init__(self,capacity):
        self.capacity=capacity
        self.d={}
        self.size=0
        self.head=DLinkedNode()
        self.tail=DLinkedNode()
        self.head.next=self.tail
        self.tail.pre=self.head

    def get(self,key):
        if key in self.d:
            self.moveToHead(self.d[key])
            return self.d[key].val
        else:
            return -1


    def put(self,key,value):
        if key in self.d:
            node=self.d[key]
            node.val=value
            self.moveToHead(node)
        else:
            if self.size<self.capacity:
                node=DLinkedNode(key,value)
                self.d[key]=node
                self.addToHead(node)
                self.size+=1
            else:
                tailkey=self.tail.pre.key
                self.d.pop(tailkey)
                self.removeTail()
                node=DLinkedNode(key,value)
                self.addToHead(node)
                self.d[key]=node


    def addToHead(self,node):
        node.next=self.head.next
        self.head.next.pre=node
        self.head.next=node
        node.pre=self.head

    def moveToHead(self,node):
        node.pre.next = node.next
        node.next.pre = node.pre

        node.next=self.head.next
        self.head.next.pre=node
        self.head.next=node
        node.pre=self.head


    def removeNode(self,node):
        node.pre.next=node.next
        node.next.pre=node.pre

    def removeTail(self):
        self.tail.pre=self.tail.pre.pre
        self.tail.pre.next=self.tail


lr=LRUCache(2)
lr.put(1,1)
lr.put(2,2)
res=lr.get(1)
print(res)
lr.put(3,3)
print(lr.get(2))
lr.put(4,4)
print(lr.get(1))
print(lr.get(3))
print(lr.get(4))
