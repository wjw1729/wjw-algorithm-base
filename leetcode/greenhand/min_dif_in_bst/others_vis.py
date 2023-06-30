# Definition for a binary tree node.

"""
how to make this easier to comprehensive?
"""
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        ans,pre=float("inf"),-1
        stack=[]
        while root or stack:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop(-1)
            if pre==-1:
                pre=root.val
            else:
                ans=min(ans,root.val-pre)
                pre=root.val
            root=root.right
        return ans

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


s=Solution()
input='[4,2,6]'
#for i in range(len(input)):
    #print(input[i])
root=stringToTreeNode(input)
#print(root)
min_val=s.minDiffInBST(root)
print(min_val)