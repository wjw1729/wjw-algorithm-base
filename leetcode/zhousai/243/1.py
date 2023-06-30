"""
author:wjw
分析：
"""

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:


        def trans(s):
            res=''
            for char in s:
                res+=str(ord(char)-ord('a'))
            return int(res)

        first=trans(firstWord)
        second=trans(secondWord)
        target=trans(targetWord)

        if first+second==target:
            return True
        else:
            return False



firstWord = "acb"
secondWord = "cba"
targetWord = "cdb"
firstWord = "aaa"
secondWord = "a"
targetWord = "aab"
firstWord = "aaa"
secondWord = "a"
targetWord = "aaaa"
res=Solution().isSumEqual(firstWord,secondWord,targetWord)
print(res)


