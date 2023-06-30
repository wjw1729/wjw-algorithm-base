"""
author:wjw
分析：基于迭代的实现方法。先将所有的left都加入栈中，逐步往上进行考虑。
"""

class Solution:
    def kthSmallest(self,root,k):
        stack=[]

        while True:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            k-=1
            if k==0:
                return root.val
            root=root.right
