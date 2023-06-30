class Solution:
    def stoneGameIX(self, stones) -> bool:
        stones = [x % 3 for x in stones]
        count_1 = 0
        count_2 = 0
        count_0 = 0

        for x in stones:
            if x == 0:
                count_0 += 1
            if x == 1:
                count_1 += 1
            if x == 2:
                count_2 += 1

        if count_1 == count_2 == 0:
            return False

        Alice = None
        allused = False

        def solve(count_1, count_2, pre, idx):
            nonlocal Alice
            nonlocal allused
            if Alice != None:
                return

            if pre == 1 and count_1 > 0:
                count_1 -= 1
                solve(count_1, count_2, 2, (idx + 1) % 2)
            elif pre == 2 and count_2 > 0:
                count_2 -= 1
                solve(count_1, count_2, 1, (idx + 1) % 2)

            else:

                if idx == 1 and not (count_1 == count_2 == 0):
                    Alice = True
                    return
                else:
                    if count_1 == count_2 == 0:
                        allused = True
                    Alice = False
                    return


        if count_1 > 0:
            solve(count_1 - 1, count_2, 1, 1)
            if Alice and count_0 % 2 == 0 or (count_0 % 2 == 1 and allused == False and not Alice):
                return True
        Alice=False
        if count_2 > 0:
            solve(count_1, count_2 - 1, 2, 1)
            if Alice and count_0 % 2 == 0 or (count_0 % 2 == 1 and allused == False and not Alice):
                return True

        return False

stones=[20,3,20,17,2,12,15,17,4]
res=Solution().stoneGameIX(stones)
print(res)