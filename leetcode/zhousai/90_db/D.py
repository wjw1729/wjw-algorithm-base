# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root, queries) :

        n=len(root)
        m=len(queries)

        @lru_cache(None)
        def dfs (node):
            if not node:
                return  0

            res=1
            res+=max(dfs(node.left),dfs(node.right))

            return res

        mapd={c:i for i,c in enumerate(queries)}

        ans=[0]*m
        q=queue()
        q.append((root,0))

        while q:
            nq=deque()
            cnt=Counter()
            max1 =0
            max2=0
            while q:
                node,l=q.popleft()

                if node.left:
                    nq.append((node.left,l+1))
                    cnt[dfs(node.left)+l+2]+=1
                    if dfs(node.left)+l+2>max1:
                        max2=max1
                        max1=dfs(node.left)+l+2
                    elif dfs(node.left)+l+2>max2:
                        max2=dfs(node.left)+l+2

                if node.right:
                    nq.append((node.right,l+1))
                    cnt[(dfs(node.right) + l + 2)]+=1
                    if dfs(node.right)+l+2>max1:
                        max2=max1
                        max1=dfs(node.right)+l+2
                    elif dfs(node.right)+l+2>max2:
                        max2=dfs(node.right)+l+2


            for x,y in nq:
                if x in mapd:
                    cnt[y+1+dfs(x)]-=1
                    if cnt[max1]>=0:
                        ans[mapd[x]]=max1
                    else:
                        ans[mapd[x]] = max2

        return ans












