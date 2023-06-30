class Solution:
    def maxChunksToSorted(self, arr) -> int:

        ans = 0
        n = len(arr)
        i = 0
        maxa = -1

        while i < n:
            tmpa = arr[i]
            pidx = i
            if tmpa == maxa:
                i += 1
                ans += 1
                continue

            while maxa != tmpa:
                maxa = tmpa
                idx = pidx
                for j in range(n - 1, pidx, -1):
                    if arr[j] < maxa:
                        idx = j
                        break
                tmpa = max(maxa, max(arr[pidx:idx], default=0))
                pidx = idx

            i = idx + 1
            ans += 1

        return ans


arr = [2, 1, 3, 4, 4]
res = Solution().maxChunksToSorted(arr)
print(res)
