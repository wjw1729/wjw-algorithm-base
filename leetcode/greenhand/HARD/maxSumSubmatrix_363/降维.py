"""
先将问题降维，降维一维探索方法，便于分析
一维解法：前缀和Si,Sr-Sl<=k的最大值
"""

import time
def max_k(list, k):
    n = len(list)
    S = [0]
    a = S[0]
    for i in range(n):
        a = a + list[i]
        S.append(a)

    max_sum = float('-inf')
    for i in range(1, n + 1):
        for j in range(0, i):
            if S[i] - S[j] <= k:
                max_sum = max(max_sum, S[i] - S[j])

    return max_sum



t1=time.time()
list = [9, -10, -3, -1, 1, 7, -6, -2, 1, -4, -6, -8, -1, 2, -9, -7, -9, -1, -1, 5, -4, 5, -8, 3, 4, 2, 9, 4, 5, 4, -8, 5,
     4, -9, -10, 3, -2, -2, 9, 0, -4, 3, 5, -10, 8, -10, 9, -7, -6, 1, 2, 6, -8, 1, 7, 3, 0, -5, 7, -6, 1, 9, -8, 4, -7,
     -9, 1, 8, -2, 6, -1, 0, 8, 4, -9, 8, -3, 7, -4, 3, -6, 2, -1, -2, -10, -10, -10, -3, 8, 2, -4, 3, -6, -3, 1, 9, -9,
     7, -6, 8]
k = 292
result = max_k(list, k)
print(result)
print(time.time()-t1)