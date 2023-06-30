from collections import defaultdict


class Solution:
    def canSeePersonsCount(self, heights):

        ans = []
        n = len(heights)

        d = defaultdict(int)
        for i in range(n - 1, 0, -1):
            if heights[i] > heights[i - 1]:
                d[i - 1] = i
            else:
                index = i
                while heights(d[index]) < heights[i - 1]:
                    index = d[index]
                d[i - 1] = i

        for i in range(n):
            tmp = 0
            maxheight = 0
            for j in range(i + 1, n):
                if maxheight < heights[j]:
                    tmp += 1
                    maxheight = heights[j]
                if heights[j] > heights[i]:
                    break

            ans.append(tmp)

        return ans