from collections import defaultdict
class Solution:
    def countHighestScoreNodes(self, parents) -> int:
        n = len(parents)
        sub = [[0, 0] for i in range(n)]

        children = defaultdict(list)

        for i in range(n):
            children[parents[i]].append(i)

        def subnodes(node):
            if children[node] == []:
                return 1
            for i in range(len(children[node])):
                sub[node][i] = subnodes(children[node][i])

            return sub[node][0] + sub[node][1]+1

        subnodes(0)
        ans = []
        for node in range(n):
            tmp = (sub[node][0] if sub[node][0] != 0 else 1) * (sub[node][1] if sub[node][1] != 0 else 1) * (
                        n - 1 - sub[node][0] - sub[node][1])
            ans.append(tmp)

        max_value = max(ans)
        res = 0
        for i in range(n):
            if ans[i] == max_value:
                res += 1

        return res

parents = [-1,2,0]
res=Solution().countHighestScoreNodes(parents)
print(res)