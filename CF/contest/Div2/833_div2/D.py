import sys
sys.setrecursionlimit()
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:

        vol = [poured]

        for _ in range(query_row):
            nvol = [0] * (len(vol) + 1)
            for j in range(len(vol) + 1):
                nvol[j] += (vol[j] - 1) / 2 if j < len(vol) and vol[j] - 1 > 0 else 0
                nvol[j] += (vol[j - 1] - 1) / 2 if j != 0 and vol[j - 1] - 1 > 0 else 0

            vol = nvol[:]

        return min(vol[j], 1)


poured=25
query_row=6
query_glass=1

res=Solution().champagneTower(poured,query_row,query_glass)
print(res)