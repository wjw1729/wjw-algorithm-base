class Solution:
    def circleGame(self, toys, circles, r):

        circleset = set()
        for cx, cy in circles:
            circleset.add((cx, cy))

        ans = 0
        for tx, ty, tr in toys:

            if tr > r:
                continue

            tmpr = r - tr

            check=False
            for x in range(tx - tmpr, tx + tmpr + 1):
                for y in range(ty - tmpr, ty + tmpr + 1):
                    if pow((x - tx) ** 2 + (y - ty) ** 2, 0.5) <= tmpr and (x, y) in circleset:
                        ans += 1
                        check=True
                        break

                if check:
                    break


        return ans

toys = [[1, 3, 4], [4, 3, 4], [7, 1, 4]]
circles = [[1, 0], [3, 3]]
r = 4

toys = [[3, 3, 1], [3, 2, 1]]
circles = [[4, 3]]
r = 2

toys=[[1,3,2],[4,3,1]]
circles=[[1,0],[3,3],[0,0],[3,4]]
r=4

res = Solution().circleGame(toys, circles, r)
print(res)

O(C*n+m),n为toys的长度,m为套圈的长度，C为一个常数项，上界4*(r-tr)**2.