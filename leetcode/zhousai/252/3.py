"""

"""


class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        total = 0
        layer = 0
        for i in range(1, 100000):
            nextlayer = layer + 8 * i - 4 + 4 * 2 * i+4*2*(i-1)
            total += nextlayer
            layer = nextlayer

            if total >= neededApples:
                return 8 * i


neededApples = 10**15

res = Solution().minimumPerimeter(neededApples)
print(res)
