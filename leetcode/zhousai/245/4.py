"""
author:wjw
分析：随机模拟算法。Monte Carlo算法
"""

import random


class Player:
    def __init__(self, a=0, b=0):
        self.power = a
        self.number = b


class Solution:
    def earliestAndLatest(self, n, firstPlayers, secondPlayers):

        if n <= 10:
            N = 800
        elif n <= 20:
            N = 8000
        else:
            N = 38000

        ans1 = 9999
        ans2 = 0



        while N > 0:
            rest = n
            p = [Player() for _ in range(n)]

            for i in range(n):
                p[i].power = random.randint(0,1000)
                p[i].number = i + 1

            p[firstPlayers - 1].power = 11000000
            p[secondPlayers - 1].power = 10999999

            turn = 1

            while rest > 1:
                for i in range((rest + 1) // 2):
                    if p[i].power < p[rest - 1 - i].power:
                        p[i] = p[rest - i - 1]
                    if p[i].number == firstPlayers and p[rest - 1 - i].number == secondPlayers:
                        ans1 = min(ans1, turn)
                        ans2 = max(ans2, turn)

                rest = (rest + 1) // 2
                turn += 1

                p = p[:rest]
                p.sort(key=lambda x: x.number)

            N -= 1

        return [ans1, ans2]


n = 11
firstPlayer = 2
secondPlayer = 4

n = 5
firstPlayer = 1
secondPlayer = 5
res = Solution().earliestAndLatest(n, firstPlayer, secondPlayer)
print(res)
