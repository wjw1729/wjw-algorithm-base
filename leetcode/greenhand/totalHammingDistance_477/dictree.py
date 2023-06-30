"""
author:wjw
分析：字典树实现,可以但没必要！
"""
class Trie:
    L=30

    def __init__(self):
        self.left=None
        self.right=None


    def insert(self,val):
        node=self
        for i in range(self.L,-1,-1):
            bit=(val>>i)&1
            if bit==0:
                if not node.left:
                    node.left=Trie()
                node=node.left
            else:
                if not node.right:
                    node.right=Trie()
                node=node.right


    def getHamDis(self,val):