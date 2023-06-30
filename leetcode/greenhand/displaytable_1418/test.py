class Solution:
    def floodFill(self, image, sr, sc, newColor: int):
        m = len(image)
        n = len(image[0])
        queue = [(sr, sc)]
        origincolor=image[sr][sc]

        while queue:
            r, c = queue.pop(0)
            for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if 0 <= x < m and 0 <= y < n and image[x][y] == origincolor:
                    queue.append((x, y))
            image[r][c] = newColor

        return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
newColor = 2
image=[[0,0,0],[0,1,1]]
sr=1
sc=1
newColor=1
res = Solution().floodFill(image, sr, sc, newColor)
print(res)
