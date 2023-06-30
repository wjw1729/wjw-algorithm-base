from collections import Counter
class Solution:
    def largestPalindromic(self, num: str) -> str:

        cnt = Counter(list(num))

        ans = []
        for k, v in sorted(cnt.items())[::-1]:
            ans += [k] * (v // 2)
            cnt[k] -= v // 2 * 2

        for k, v in sorted(cnt.items())[::-1]:
            if v % 2 == 1:
                ans += [k]
                break

        return ''.join(ans + ans[:-1][::-1]).strip('0')

num = "444947137"
res=Solution().largestPalindromic(num)
print(res)