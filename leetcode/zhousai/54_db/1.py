class Solution:
    def isCovered(self, ranges, left: int, right: int) -> bool:

        ans = []
        ranges.sort(key=lambda x: x[0])
        n = len(ranges)
        range_left = ranges[0][0]
        range_right = ranges[0][1]
        for i in range(1, n):
            if range_right >= ranges[i][0] - 1:
                range_right = max(range_right,ranges[i][1])
            else:
                ans.append([range_left, range_right])
                range_left = ranges[i][0]
                range_right = ranges[i][1]

        ans.append([range_left, range_right])

        for qujian in ans:
            if left >= qujian[0] and right <= qujian[1]:
                return True
        return False

ranges=[[1,50]]
left=1
right=50
ranges=[[25,42],[7,14],[2,32],[25,28],[39,49],[1,50],[29,45],[18,47]]

left=15
right=38
res=Solution().isCovered(ranges,left,right)
print(res)