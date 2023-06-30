class Solution:
    def maximumPopulation(self, logs) -> int:

        maxnum = 0

        n = len(logs)
        logs.sort(key=lambda x: x[0])
        right = logs[0][1]
        left = logs[0][0]
        num = 1
        ans = left
        for i in range(1,n):
            if right > logs[i][0]:
                num += 1
                left = max(left, logs[i][0])
                if num > maxnum:
                    maxnum = num
                    ans = left
            else:
                right = logs[i][1]
                left = logs[i][0]
                num = 1
        return ans


logs = [[1982, 1998], [2013, 2042], [2010, 2035], [2022, 2050], [2047, 2048]]
logs=[[2025,2041],[1988,2007],[2003,2046],[2045,2049],[2025,2027],[2014,2040],[2014,2027],[2011,2027],[1972,2019]]
res = Solution().maximumPopulation(logs)
print(res)
