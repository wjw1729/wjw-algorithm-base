from functools import reduce

ans=[[1]*i for i in range(1,5)]
print(1)

a=reduce(lambda x,y:x*y,range(1,5))
print(a)


def cni(n, i):
    return reduce(lambda x, y: x * y, range(n - i + 1, n + 1),1) // reduce(lambda x, y: x * y, range(1, i + 1),1)

print(cni(3,0))