class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ans = 0

        n = len(word)
        for i in range(n - 5):
            for j in range(i + 5, n + 1):
                validset = ['a', 'e', 'i', 'o', 'u']
                elset = [chr(97 + i) for i in range(26) if chr(97 + i) not in validset]
                if all(x in word[i:j] for x in validset) and not any(x in word[i:j] for x in elset):
                    ans += 1

        return ans


word = "aeiouu"
word="duuebuaeeeeeeuaoeiueaoui"
res=Solution().countVowelSubstrings(word)
print(res)