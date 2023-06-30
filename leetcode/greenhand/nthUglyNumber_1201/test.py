def getcmd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


def getgongbei(a, b):
    return a * b // getcmd(a, b)


class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        left = 0
        right = min(a, b, c) * n

        while left <= right:
            mid = (left + right) // 2
            if (mid // a + mid // b + mid // c - mid // getgongbei(a, b) - mid // getgongbei(a, c) - mid // getgongbei(
                    b, c) + mid // getgongbei(getgongbei(a, b), c)) < n:
                left = mid + 1
            else:
                right = mid - 1
        return right + 1


n = 1000000000
a = 2
b = 217983653
c = 336916467
n = 4
a = 2
b = 3
c = 4
res = Solution().nthUglyNumber(n, a, b, c)
print(res)
print(res // a + res // b + res // c)
