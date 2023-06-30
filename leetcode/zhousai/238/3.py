class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:

        tmp = 0
        pre = 'a'
        rest = {'a', 'e', 'i', 'o', 'u'}

        ans = 0

        for ch in word:
            if ch < pre:
                if not rest:
                    ans = max(ans, tmp)
                tmp = 1
                rest = {'a', 'e', 'i', 'o', 'u'}
                rest.remove(ch)
                pre = ch
            else:
                tmp += 1
                if ch in rest:
                    rest.remove(ch)
                pre = ch
        if not rest:
            ans=max(ans,tmp)
        return ans

word="aeiaaioaaaaeiiiio"
res=Solution().longestBeautifulSubstring(word)
print(res)