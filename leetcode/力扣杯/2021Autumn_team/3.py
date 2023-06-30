from collections import defaultdict
class Solution:
    def volunteerDeployment(self, finalCnt, totalNum: int, edges, plans):

        adjacent = defaultdict(list)
        for u, v in edges:
            adjacent[u].append(v)
            adjacent[v].append(u)

        def initTotal(finalCnt, x):
            finalCnt = [x] + finalCnt

            for op, idx in plans[::-1]:
                if op == 1:
                    finalCnt[idx] *= 2
                elif op == 2:
                    for v in adjacent[idx]:
                        finalCnt[v] -= finalCnt[idx]
                else:
                    for v in adjacent[idx]:
                        finalCnt[v] += finalCnt[idx]

            return sum(finalCnt)

        l = 0
        r = 10 ** 9

        if initTotal(finalCnt, l) < initTotal(finalCnt, r):
            positive = True
        elif initTotal(finalCnt, l) < initTotal(finalCnt, r):
            positive = False
        else:
            print(1)

        while l <= r:
            mid = (l + r + 1) // 2
            if positive:
                if initTotal(finalCnt, mid) < totalNum:
                    l = mid + 1
                elif initTotal(finalCnt, mid) > totalNum:
                    r = mid - 1
                else:
                    break
            else:
                if initTotal(finalCnt, mid) > totalNum:
                    l = mid + 1
                elif initTotal(finalCnt, mid) < totalNum:
                    r = mid - 1
                else:
                    break

        finalCnt = [mid] + finalCnt
        for op, idx in plans[::-1]:
            if op == 1:
                finalCnt[idx] *= 2
            elif op == 2:
                for v in adjacent[idx]:
                    finalCnt[v] -= finalCnt[idx]
            else:
                for v in adjacent[idx]:
                    finalCnt[v] += finalCnt[idx]

        return finalCnt


finalCnt = [4, 13, 4, 3, 9]
totalNum = 54
edges = [[0, 3], [1, 3], [4, 3], [2, 3], [2, 5]]
plans = [[1, 1], [3, 3], [2, 5], [1, 0]]

res = Solution().volunteerDeployment(finalCnt, totalNum, edges, plans)
print(res)
