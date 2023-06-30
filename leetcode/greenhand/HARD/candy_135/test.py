from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        ans = 0
        counter = defaultdict(int)
        maxcounter = s[0]

        for right in range(len(s)):
            counter[s[right]] += 1
            if counter[s[right]] >= counter[maxcounter]:
                maxcounter = s[right]
            while right - left + 1 - counter[maxcounter] > k:
                counter[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
s='BAAA'
res=Solution().characterReplacement(s,0)
print(res)