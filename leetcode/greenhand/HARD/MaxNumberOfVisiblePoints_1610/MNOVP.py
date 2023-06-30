"""
确定其实边，二分搜索。
"""

# 依据夹角进行二分
import math
from collections import defaultdict
import bisect


class Solution:
    def visiblePoints(self, points, angle: int, location) -> int:

        def get_angle(x, y):
            if x == 0:
                return 90 if y > 0 else -90
            if x > 0:
                return math.atan(y / x) * 180 / math.pi
            elif x < 0:
                return 180 + math.atan(y / x) * 180 / math.pi

        ans = 0
        angles = set()
        counter = defaultdict(int)
        for x, y in points:
            if x == location[0] and y == location[1]:
                ans += 1
                continue
            ang = get_angle(x - location[0], y - location[1])
            ang += 360 if ang < 0 else 0
            angles.add(ang)
            counter[ang] += 1

        angles = list(angles)
        angles.sort()
        maxang = max(angles)
        res_angles = []
        for x in angles:
            if x + 360 <= maxang + angle:
                res_angles.append(x + 360)
                counter[x+360]=counter[x]
            else:
                break
        angles.extend(res_angles)

        pre_counter = dict()
        total = 0
        for ag in angles:
            total += counter[ag ]
            pre_counter[ag] = total

        tmp_ans = 0
        for st in angles:
            idx = bisect.bisect_right(angles, st + angle)
            end = angles[idx - 1]
            tmp_ans = max(tmp_ans, pre_counter[end] - pre_counter[st] + counter[st])

        return ans + tmp_ans

points=[[68,61],[63,4],[20,64],[13,6],[47,77],[11,23],[73,40],[34,45],[24,89],[85,68],[18,4],[87,41],[1,12],[87,72],[7,84],[75,64],[76,59],[62,36],[78,18],[37,71],[47,49],[9,21],[62,31],[12,33],[91,39],[45,67],[73,95],[36,75],[54,25],[32,2],[51,38],[71,29],[50,87],[3,64],[92,47],[10,26],[7,56],[81,56]]
angle=42
location=[9,61]
res=Solution().visiblePoints(points,angle,location)
print(res)










