def get_mod(a, b, c):
    res = 1
    temp = a
    while b > 0:
        if b & 1:
            res = (res * temp) % c
        temp = (temp * temp) % c
        b >>= 1

    return res


from collections import Counter


class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        d = Counter(nums)
        dup = sorted(d.items(), key=lambda x: x[1], reverse=True)[0][0]
        ans = set(range(1, n + 1)) - set(nums)
        return [dup, ans.pop()]
        


nums = [1, 2, 2, 4]
res = Solution().findErrorNums(nums)
print(res)
