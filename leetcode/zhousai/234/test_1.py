import bisect


class Solution:
    def closestCost(self, baseCosts, toppingCosts, target: int) -> int:

        toppingCosts.sort()
        minbase = min(baseCosts)
        valueset = set()
        valueset.add(0)
        for cost in toppingCosts:
            nextvalues = set()
            for v in valueset:
                for i in range(1, 3):
                    if i * cost + v not in valueset:
                        nextvalues.add(i * cost + v)

                    if minbase + i * cost + v > target:
                        break
            valueset |= nextvalues

        valuels = list(valueset)
        valuels.sort()
        n = len(valuels)
        ans = float('inf')
        mingap = float('inf')
        for base in baseCosts:
            index = bisect.bisect(valuels, target - base)
            left = base + valuels[index - 1] if index > 0 else float('inf')
            right = base + valuels[index] if index < n else float('inf')
            if right - target < mingap:
                ans = right
                mingap = right - target
            elif right - target == mingap:
                ans = min(ans, right)

            if target - left < mingap:
                ans = left
                mingap = target - left
            elif target - left == mingap:
                ans = min(ans, left)

        return ans


baseCosts = [3,10]
toppingCosts = [2,5]
target = 9

res=Solution().closestCost(baseCosts,toppingCosts,target)
print(res)