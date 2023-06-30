from collections import defaultdict, deque


class Solution:
    def rootCount(self, edges, guesses, k: int) -> int:

        ans = 0
        res = 0
        cnt = defaultdict(int)
        for s, t in guesses:
            cnt[(s, t)] += 1

        g = defaultdict(list)

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        q = deque()
        q.append(0)
        vis = {0}
        while q:
            u = q.popleft()

            for v in g[u]:
                if v not in vis:
                    ans += cnt[(u, v)]
                    q.append(v)
                    vis.add(v)

        if ans >= k:
            res += 1

        rcnt = defaultdict(int)
        rcnt[0] = ans

        q = deque()
        q.append(0)
        vis = {0}

        while q:
            u = q.popleft()

            for v in g[u]:
                if v not in vis:
                    q.append(v)
                    tmp = rcnt[u] - cnt[(u, v)]
                    tmp += cnt[(v, u)]
                    rcnt[v]=tmp
                    if tmp >= k:
                        res += 1
                    vis.add(v)

        return res
edges = [[0,1],[1,2],[1,3],[4,2]]
guesses = [[1,3],[0,1],[1,0],[2,4]]
k = 3
res=Solution().rootCount(edges,guesses,k)
print(res)