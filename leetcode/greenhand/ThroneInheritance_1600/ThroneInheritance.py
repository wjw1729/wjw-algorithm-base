"""
author：wjw
分析：掌握defaultdict(list)的用法，以及如何书写一个类，属性和方法+先序遍历
"""



from collections import defaultdict

class ThroneInheritance:
    def __init__(self, kingName: str):
        self.tree = defaultdict(list)
        self.king = kingName
        self.dead = set()

    def birth(self, parentName: str, childName: str):
        self.tree[parentName].append(childName)

    def death(self, name):
        self.dead.add(name)

    def getInheritanceOrder(self):
        ans = []

        def preorder(name):
            if name not in self.dead:
                ans.append(name)
            for child in self.tree[name]:
                preorder(child)

        preorder(self.king)

        return ans


t = ThroneInheritance("king")
t.birth("king", "andy")
t.birth("king", "bob")
t.birth("king", "catherine")
t.birth("andy", "matthew")
t.birth("bob", "alex")
t.birth("bob", "asha")
res1 = t.getInheritanceOrder()
t.death("bob")
res2 = t.getInheritanceOrder()

print(res1)
print(res2)
