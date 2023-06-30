"""
author:wjw
分析：加入条件可旋转的
"""

import bisect


class Solution:
    def maxEnvelopes(self, envelopes):

        envelopes = [(h, w) if h < w else (w, h) for h, w in envelopes]

        envelopes.sort(key=lambda x: (x[0], -x[1]))

        lis = []
        for _, w in envelopes:
            idx = bisect.bisect_left(lis, w)
            if idx == len(lis):
                lis.append(w)
            else:
                lis[idx] = w

        return len(lis)


envelopes = [[5, 4], [6, 4], [6, 7], [2, 3]]
# envelopes=[[6,7],[5,3],[2,4],[1,1]]
res = Solution().maxEnvelopes(envelopes)
print(res)
