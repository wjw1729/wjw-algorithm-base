from collections import defaultdict
class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        als = ['Q', 'W', 'E', 'R']
        cnt = defaultdict(int)
        cntt = 0

        for i in range(4):
            cnt[als[i]] = s.count(als[i])
            if cnt[als[i]] > n // 4:
                cntt += cnt[als[i]] - n // 4
        pls = []

        for i in range(n):
            if cnt[s[i]] > n // 4:
                pls.append(i)
        if cntt == 0:
            return 0
        ans = float('inf')

        print(cntt, pls)
        for i in range(len(pls)):
            if i + cntt - 1 < len(pls):
                ans = min(ans, pls[i + cntt - 1] - pls[i] + 1)
            else:
                break

        return ans


s ="WWWEQRQEWWQQQWQQQWEWEEWRRRRRWWQE"
res=Solution().balancedString(s)
print(res)
