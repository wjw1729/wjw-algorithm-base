from collections import defaultdict
class Solution:
    def smallestMissingValueSubtree(self, parents, nums) :
        tree = defaultdict(list)

        for u, v in enumerate(parents):
            tree[v].append(u)

        n = len(nums)
        values = [set() for _ in range(n)]

        def dfs(u):

            res = {nums[u]}

            for v in tree[u]:
                dfs(v)
                res |= values[v]

            values[u] |= res

        dfs(0)

        ans = []
        for a in values:
            for i in range(1, max(nums) + 2):
                if i not in a:
                    ans.append(i)
                    break
        return ans

parents = [-1,0,0,2]
nums = [1,2,3,4]
res=Solution().smallestMissingValueSubtree(parents,nums)
print(res)