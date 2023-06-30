class Solution:
    def findRepeatedDnaSequences(self, s: str) :
        n = len(s)
        pre = set()
        ans = set()

        for i in range(n - 9):
            if s[i:i + 10] not in pre:
                pre.add(s[i:i + 10])
            else:
                ans.add(s[i:i + 10])

        return list(ans)


s="AAAAAAAAAAA"
res=Solution().findRepeatedDnaSequences(s)
print(res)