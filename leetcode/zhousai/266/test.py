class Solution:
    def checkPartitioning(self, s: str) -> bool:

        n = len(s)

        for i in range(n - 2):

            if s[i] == s[0]:
                if s[:i + 1] == s[:i+1][::-1]:
                    for j in range(i + 2, n):
                        if s[j] == s[-1]:
                            if i==0 and j==n-2:
                                print(1)
                            if s[i + 1:j] == s[i+1:j][::-1] and s[j:] == s[j:][::-1]:

                                return True

        return False

s="abcbdd"
res=Solution().checkPartitioning(s)
print(res)