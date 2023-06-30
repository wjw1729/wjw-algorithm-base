"""
author:wjw
分析：掌握string.find(str)函数即可
"""

class Solution:
    def strStr(self,haystack,needle):
        if needle=='':
            return 0
        if needle not in haystack:
            return -1
        index=haystack.find(needle)
        return index




haystack='aaaa'
needle='bba'
res=Solution().strStr(haystack,needle)
print(res)

