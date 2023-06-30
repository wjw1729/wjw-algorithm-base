class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)

        def minflips(x):
            tnum = 0
            fnum = 0
            for i in range(x):
                if answerKey[i] == 'T':
                    tnum += 1
                else:
                    fnum += 1
            ans = min(tnum, fnum)

            for r in range(x, n):
                if answerKey[r] == 'T':
                    tnum += 1
                else:
                    fnum += 1
                if answerKey[r - x] == 'T':
                    tnum -=1
                else:
                    fnum -= 1
                ans = min(ans, min(tnum, fnum))
            return ans

        l = 1
        r = n

        print(minflips(34))
        while l <= r:
            mid = (l + r + 1) // 2

            if minflips(mid) <= k:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans



answerKey="FFTFTTTFFTTTTFTTFFTFTTFTFTTFFFTTTTFFFTFFFFTTFTFTTFFFFTFTFTFTTFFTFFTFFFFFFTTFFTFFTFFTFFFFFTFTTFFTTFTT"
k=10
res=Solution().maxConsecutiveAnswers(answerKey,k)
print(res)
