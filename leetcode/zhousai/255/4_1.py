"""

"""
import itertools


class Solution:
    def recoveryArray(self, n, sums):

        def solvenonnegative(n, sums):
            ans = []
            sums.remove(0)

            while len(ans) < n:
                x = min(sums)

                for i in range(len(ans) + 1):
                    tmp = [sum(y) + x for y in itertools.combinations(ans, i)]
                    for j in tmp:
                        sums.remove(j)
                ans.append(x)

            return ans

        m = min(sums)
        sums = [x - m for x in sums]

        tmp = solvenonnegative(n, sums)
        if m == 0:
            return tmp

        for i in range(len(tmp) + 1):
            for y in itertools.combinations(tmp, i):
                if sum(y) == -m:
                    for num in y:
                        tmp.remove(num)
                        tmp.append(-num)
                    return tmp


n = 4
sums = [0, 1, 1, 2, 2, 3, 3, 4, 5, 6, 6, 7, 7, 8, 8, 9]
n = 3
sums = [-3, -2, -1, 0, 0, 1, 2, 3]
"""
n = 2
sums = [0, 0, 0, 0]
n = 4
sums = [0, 0, 5, 5, 4, -1, 4, 9, 9, -1, 4, 3, 4, 8, 3, 8]
"""
res = Solution().recoveryArray(n, sums)
print(res)
