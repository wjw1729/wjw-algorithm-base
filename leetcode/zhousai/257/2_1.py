"""

"""


class Solution:
    def numberOfWeakCharacters(self, properties):
        properties.sort(key=lambda x: (-x[0], x[1]))

        maxdf = 0
        ans = 0
        for at, df in properties:

            if maxdf > df:
                ans += 1
            else:
                maxdf = df

        return ans


properties = [[5, 5], [6, 3], [3, 6]]
properties= [[1,5],[10,4],[4,3]]
res = Solution().numberOfWeakCharacters(properties)
print(res)
