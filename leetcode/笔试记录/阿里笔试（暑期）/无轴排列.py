#阿里笔试。（无轴排列）
"""
1-n的排列。a[i]!=i（下标从一开始）的排列称为无轴排列。
从小到大的前k个排列。
n<1000
k<1000。
n*k<10**5

#python最大递归深度996

"""
#标准全排列的做法。
class Solution:
    def noaxispermutation(self,n,k):


        ans=[]
        nums=list(range(n))

        def dfs(nums,path):
            if not nums:
                ans.append(path[:])
                return

            if len(ans)==k:
                return

            n=len(nums)

            for i in range(n):
                val=nums.pop(i)
                if val!=len(path):
                    path.append(val)
                    dfs(nums,path)
                    path.pop()

                nums.insert(i,val)


        dfs(nums,[])

        m=len(ans)
        n=len(ans[0])
        for i in range(m):
            for j in range(n):
                ans[i][j]+=1
        return  ans

n=997#太大会超过递归深度
k=10
res=Solution().noaxispermutation(n,k)
print(res)





