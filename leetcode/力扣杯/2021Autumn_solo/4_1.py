from collections import defaultdict


class Solution:
    def circleGame(self, toys, circles, r: int) -> int:

        hashmap = defaultdict(set)

        for tx, ty, tr in toys:
            hashmap[tr].add((tx, ty))

        ans = 0

        for tr in sorted(hashmap.keys()):
            if tr > r:
                break

            tmp_r = r - tr

            validpoints = set()
            tmp = 0
            check = False
            for cx, cy in circles:
                for x in range(cx - tmp_r, cx + tmp_r + 1):
                    for y in range(cy - tmp_r, cy + tmp_r + 1):
                        if pow((x - cx) ** 2 + (y - cy) ** 2, 0.5) <= tmp_r:
                            if (x, y) in hashmap[tr] and (x,y) not in validpoints:
                                tmp += 1
                            if tmp == len(hashmap[tr]):
                                check = True
                                break
                            validpoints.add((x, y))

                    if check:
                        break
                if check:
                    break

            ans += tmp

        return ans


toys = [[1, 3, 4], [4, 3, 4], [7, 1, 4]]
circles = [[1, 0], [3, 3]]
r = 4
"""
toys = [[3, 3, 1], [3, 2, 1]]
circles = [[4, 3]]
r = 2

toys=[[1,3,2],[4,3,1]]
circles=[[1,0],[3,3],[0,0],[3,4]]
r=4
"""
res = Solution().circleGame(toys, circles, r)
print(res)
