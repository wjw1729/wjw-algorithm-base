class Solution:
    def numberOfWeakCharacters(self, properties) -> int:

        properties.sort(key=lambda x: (-x[0], -x[1]))

        search_ls = []
        n = len(properties)

        ans = 0
        for i in range(n):
            at = properties[i][0]
            df = properties[i][1]

            left = 0
            right = len(search_ls) - 1
            while left <= right:
                mid = (left + right + 1) // 2
                if search_ls[mid][0] > at and search_ls[mid][1] > df:
                    ans += 1
                    break

                if search_ls[mid][0] <= at:
                    right = mid - 1

                if search_ls[mid][1] <= df:
                    left = mid + 1

            if not search_ls or (at < search_ls[-1][0] and df > search_ls[-1][1]):
                search_ls.append([at, df])

        return ans


properties = [[8, 1], [5, 10], [5, 8], [10, 6], [1, 6], [10, 1]]
    #properties=[[4,10],[2,2],[8,8],[10,2],[5,5],[9,10],[2,6]]
#properties=[[5,5],[6,3],[3,6]]
res = Solution().numberOfWeakCharacters(properties)
print(res)
