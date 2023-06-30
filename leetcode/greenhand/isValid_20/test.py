class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        for i in range(n - 1, -1, -1):
            if s[i].isalpha():
                right_alpha = i
                break

        right = s.rfind(' ', 0, right_alpha)
        return right_alpha - right


s = " "
res = Solution().lengthOfLastWord(s)
print(res)
