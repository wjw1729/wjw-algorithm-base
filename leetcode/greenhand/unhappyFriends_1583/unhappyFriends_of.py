"""
author:wjw
分析：这里的order二维列表记录的是order[x][y]中y所处在的x的亲密度列表中的位置。
时间复杂度：O(n**2)。
"""


class Solution:
    def unhappyFriends(self, n, preferences, pairs):
        order = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n - 1):
                order[i][preferences[i][j]] = j

        match = [0] * n

        for x, y in pairs:
            match[x] = y
            match[y] = x

        ans = 0
        for x in range(n):
            y = match[x]
            index = order[x][y]

            for j in range(index):
                u = preferences[x][j]
                v = match[u]

                if order[u][x] < order[u][v]:
                    ans += 1
                    break
        return ans


n = 4
preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
pairs = [[0, 1], [2, 3]]

n = 4
preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]]
pairs = [[1, 3], [0, 2]]

res = Solution().unhappyFriends(n, preferences, pairs)
print(res)
