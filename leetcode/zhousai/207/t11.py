class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows) :

        ans = 0
        ansls = []

        for mask in range(1 << 12):
            if bin(mask).count('1') > numArrows:
                continue
            bobs = [0] * 12
            score = 0
            for i in range(1 << 12):
                if mask & (1 << i):
                    bobs[i] = aliceArrows[i] + 1
                    score += i

            total = sum(bobs)
            if total <= numArrows:
                if score > ans:
                    ansls = bobs[:]
                    if total < numArrows:
                        ansls[0] += numArrows - total
                    ans = score

        return ansls


numArrows=7
aliceArrows=[0,1,0,2,0,0,0,0,2,0,2,0]
res=Solution().maximumBobPoints(numArrows,aliceArrows)
print(res)