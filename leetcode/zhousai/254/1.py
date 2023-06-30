from collections import Counter
class Solution:
    def numOfStrings(self, patterns, word):
        counter = Counter(patterns)
        n = len(word)
        ans = 0
        for k, v in counter.items():
            length = len(k)
            for i in range(n - length + 1):
                if word[i:i + length] == k:
                    ans += v
                    break

        return ans


patterns = ["a", "abc", "bc", "d"]
word = "abc"
res = Solution().numOfStrings(patterns, word)
print(res)
