class binaryindextree:
    def __init__(self, n):
        self.n = n
        self.c = [0] * (1 + n)

    def lowbit(self, x):
        return x & -x

    def update(self, x, val):

        while x < self.n + 1:
            self.c[x] += val
            x += self.lowbit(x)

    def query(self, x):
        res = 0
        while x > 0:
            res += self.c[x]
            x -= self.lowbit(x)

        return res


def numsofforth(nums):
    res = 0

    bint = binaryindextree(n)
    pre = [0] * n

    for i in range(n):
        pre[i] = bint.query(nums[i])
        bint.update(nums[i], 1)

    suf = [nums[i] - pre[i] - 1 for i in range(n)]

    for c in range(n):
        for b in range(c):
            if nums[b] > nums[c]:
                suf[b] -= 1

        presum = [0] * (n + 1)
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + suf[i - 1]

        for a in range(c):
            if nums[a] < nums[c]:
                res += presum[c] - presum[a + 1]

    return res


t = int(input())
for _ in range(t):
    n = int(input())
    nums = [int(x) for x in input().split()]
    res = numsofforth(nums)
    print(res)
