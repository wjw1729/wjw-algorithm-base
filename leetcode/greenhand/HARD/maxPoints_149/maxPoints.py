"""
author:wjw
分析：记录斜率，统计数量，斜率保存用(mx,my),将二维转为一维。mx和my的范围为[-2*10^4,2*10^4]，val=my+mx*(2*10^4+1)
"""


def gcd(a, b):
    return gcd(b, a % b) if b != 0 else a


class Solution:
    def maxpoints(self, points):

        n = len(points)
        if n <= 2:
            return n
        ans = 0

        for i in range(n):
            d = {}
            if ans > n // 2 or ans > n - i:
                break
            for j in range(i + 1, n):

                my = points[j][1] - points[i][1]
                mx = points[j][0] - points[i][0]
                sign = 1
                if my * mx < 0:
                    sign = -1

                gcdivisor = gcd(abs(mx), abs(my))

                mx = abs(mx) / gcdivisor
                my = sign * abs(my) / gcdivisor
                val = my + mx * (20001)

                if val in d:
                    d[val] += 1
                    ans = max(ans, d[val])
                else:
                    d[val] = 2
                    ans = max(ans, d[val])

        return ans


points = [[1, 1], [2, 2], [3, 3]]
points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
points = [[0, 0]]
points = [[0, 0], [4, 5], [7, 8], [8, 9], [5, 6], [3, 4], [1, 1]]
res = Solution().maxpoints(points)
print(res)
