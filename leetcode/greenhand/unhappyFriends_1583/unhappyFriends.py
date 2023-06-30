"""
author:wjw
分析：rank[i][j]记录的是两个人i,j之间的亲密度指数矩阵。分为n-1~1个级别，越大越亲密。
    时间复杂度:O(n**2)
"""


class Solution:
    def unhappyFriends(self, n, preferences, pairs):

        rank = [[0] * n for _ in range(n)]

        for i in range(n):
            k = n - 1
            for j in preferences[i]:
                rank[i][j] = k
                k -= 1

        unhappymen = set()

        for i in range(n // 2):
            x, y = pairs[i]

            for u, v in pairs[i + 1:]:
                if rank[x][u] > rank[x][y] and rank[u][x] > rank[u][v]:
                    unhappymen.add(x)
                    unhappymen.add(u)

                if rank[x][v] > rank[x][y] and rank[v][x] > rank[v][u]:
                    unhappymen.add(x)
                    unhappymen.add(v)

                if rank[y][u] > rank[y][x] and rank[u][y] > rank[u][v]:
                    unhappymen.add(y)
                    unhappymen.add(u)

                if rank[y][v] > rank[y][x] and rank[v][y] > rank[v][u]:
                    unhappymen.add(y)
                    unhappymen.add(v)

        return len(unhappymen)


n = 4
preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
pairs = [[0, 1], [2, 3]]

n = 4
preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]]
pairs = [[1, 3], [0, 2]]

res = Solution().unhappyFriends(n, preferences, pairs)
print(res)
