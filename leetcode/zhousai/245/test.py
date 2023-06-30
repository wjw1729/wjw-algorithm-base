"""
有趣的问题：
关于a(i)=2*b(i-1),b(i)=a(i-1)+b(i-1)这样的等式，我们如果通过数学分析的方法，要通过编写怎样的程序才能得到我们想要的值呢？
1.递归互相调用的方法。当i变大时似乎不太行？
2.
"""

from functools import lru_cache


@lru_cache(None)
def a(i):
    if i == 0:
        return 1
    return 2 * b(i - 1)


@lru_cache(None)
def b(i):
    if i == 0:
        return 1
    return a(i - 1) + b(i - 1)


print(a(55))
