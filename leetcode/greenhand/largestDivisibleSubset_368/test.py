"""
如何从一个列表中找到x的最大约数
"""


def divisor(l1, k):
    for i in reversed(range(len(l1))):
        if k != l1[i] and k % l1[i] == 0:
            return l1[i]


l1=[3,4,16,8]
l2=[3,16]
l1.remove(i for i in l2)
print(sorted(l1))