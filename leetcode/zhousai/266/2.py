class Solution:
    def countVowels(self, word: str) -> int:

        ans = 0
        validset = {'a', 'e', 'i', 'o', 'u'}
        n = len(word)
        for i in range(n):
            if word[i] in validset:
                left = i + 1
                right = n - i
                ans += left * right

        return ans

word = "aba"
res=Solution().countVowels(word)
print(res)