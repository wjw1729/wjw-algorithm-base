"""
author:wjw
分析：时间不够了，要回去摔交交了，先暴力吧
思路：根据target和range(1,n+1)一次变化前的差异，得到k，再magic——operation比较即可
写的跟坨屎一样的。
优化点：找k取值的地方可以优化
"""
import time


def magic(n, k):
    out = []

    l = list(range(1, n + 1))
    while l:
        l2 = l[0:n + 1:2]
        l3 = l[1::2]
        l = l3 + l2
        for i in range(k):
            if l:
                out.append(l.pop(0))

    return out


class Solution:
    def isMagic(self, target):
        n = len(target)

        l = list(range(1, n + 1))

        l2 = l[0:n + 1:2]
        l3 = l[1::2]
        l = l3 + l2

        k = n
        for i in range(n):
            if target[i] != l[i]:
                k = i
                print(k)
                break
        if k == 0:
            return False
        if magic(n, k) == target:
            return True

        return False


t1 = time.time()
target = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56,
          58, 60, 62, 64, 66, 68, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45,
          47, 49, 51, 55, 59, 63, 67, 53, 57, 61, 65, 69]
res = Solution().isMagic(target)
print(res)
print(time.time() - t1)
