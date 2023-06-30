"""
跟着官方思路进行下去，其实答案可以了，但是就是需要释放缓存，
"""
import time


def f(s1, s2):
    if s1 == s2:
        return True

    n = len(s1)

    for i in range(1, n):
        if f(s1[0:i], s2[0:i]) and f(s1[i:], s2[i:]):
            return True

    for i in range(1, n):
        if f(s1[0:i], s2[n - i:]) and f(s1[i:], s2[0:n - i]):
            return True
    return False


t1 = time.time()

str1 = "abcdefghijklmnopq"
str2 = "efghijklmnopqcadb"
result = f(str1, str2)
print(result)
print(time.time() - t1)
