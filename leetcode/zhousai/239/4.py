

class Solution:
    def minInterval(self, intervals, queries):

        queries = list(enumerate(queries))
        queries.sort(key=lambda x: (x[1]))

        m = len(queries)

        parent = list(range(m+1))

        def find(x):
            if parent[x]==x:
                return x
            else:
                return find(parent[x])



        intervals.sort(key=lambda x: x[1] - x[0])

        ans = [-1] * m
        for left, right in intervals:
            l = 0
            r = m - 1

            index=m
            while l <= r:
                mid = (l + r + 1) // 2

                if queries[mid][1] < left:
                    l = mid + 1
                else:
                    r = mid - 1
                    index = mid

                index=find(index)
            while index < m and queries[index][1] <= right:

                if parent[index] == index:
                    ans[queries[index][0]] = right - left + 1

                    parent[index] = index + 1


                index = find(index)

        return ans

intervals = [[1,4],[2,4],[3,6],[4,4]]
queries = [2,3,4,5]
intervals=[[6,6],[5,5],[10,10],[3,6],[9,9]]
queries=[7,9,2,4,5]

res=Solution().minInterval(intervals,queries)
print(res)