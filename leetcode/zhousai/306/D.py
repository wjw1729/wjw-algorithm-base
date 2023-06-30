f = [1] * 11
for i in range(1, 11):
    f[i] = f[i - 1] * i


def ani(n, i):
    return f[n] // f[n - i]


class Solution:
    def countSpecialNumbers(self, n: int) -> int:

        def get(tmp):

            bitlen = 0
            while tmp >= 1:
                tmp //= 10
                bitlen += 1
            return bitlen

        bitlen = get(n)

        ans = 0
        for i in range(1, bitlen):
            ans += ani(10, i) - ani(9, i - 1)

        tmpn = str(n)
        vis = set()

        # print(ans)
        for i in range(bitlen):
            if i == 0:
                ans += (int(tmpn[0]) - 1) * ani(9, bitlen - 1)

            else:
                if int(tmpn[i - 1]) in vis:
                    break
                vis.add(int(tmpn[i - 1]))
                a = int(tmpn[i]) - len([x for x in vis if x < int(tmpn[i])])
                ans += a * ani(9 - i, bitlen - 1 - i)

            # print(ans)

        return ans + (1 if len(set(tmpn)) == bitlen else 0)





