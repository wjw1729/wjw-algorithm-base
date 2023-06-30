from collections import defaultdict
class Solution:
    def numOfPairs(self, nums, target: str) -> int:

        def strsub(s1, s2):
            l1 = len(s1)
            l2 = len(s2)

            if s2 == s1[:l2]:
                return s1[l2:]

            return None

        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

        ans = 0
        for k, v in counter.items():
            tmp = strsub(target, k)
            if tmp != None:
                if tmp != k:
                    ans += v * counter[tmp]
                else:
                    ans += v * (v - 1)
        return ans

nums=["88760205","88","8","7602058"]
target="887602058"
res=Solution().numOfPairs(nums,target)
print(res)
