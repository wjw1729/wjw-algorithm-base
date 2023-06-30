"""

"""

class Solution:
    def pacificAtlantic(self, heights):
        # 将图中的点分为四类，能够流到大西洋、太平洋、大西洋和太平洋、都不能。
        # 对图中的结点进行L字式的向内更新信息。分别对大西洋、太平洋进行更新。
        # 并查集？

        m = len(heights)
        n = len(heights[0])

        def judge(r, c):
            queue = [(r, c)]
            bin={(r,c)}
            Pacific = False
            Atlantic = False

            while queue:
                r, c = queue.pop()
                if r == 0 or c == 0:
                    Pacific = True
                if r == m - 1 or c == n - 1:
                    Atlantic = True
                if Pacific and Atlantic:
                    return True
                for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= x < m and 0 <= y < n and heights[x][y] <= heights[r][c] and (x,y) not in bin:
                        queue.append((x, y))
                        bin.add((x,y))
            return False

        ans = []
        for i in range(m):
            for j in range(n):
                if judge(i, j):
                    ans.append([i, j])

        return ans


heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
res = Solution().pacificAtlantic(heights)
print(res)
