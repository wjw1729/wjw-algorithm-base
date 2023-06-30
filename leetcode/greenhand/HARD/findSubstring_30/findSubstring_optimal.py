"""
author:lc toprank
分析：用长度为tlen的滑动窗口进行考察，窗口起始节点的位置依据%(wlen)的模分为wlen类，每一类分别进行分析。考察整个滑动窗口是否符合要求时，从右端开始进行考察，一旦不符合就将整个滑动窗口的左端移动到
    该处，继续判断。直到超出字符串的范围。
    时间复杂度:O(nm).其中m为words中字符串的长度，n为s长度。
"""
from collections import Counter


class Solution:
    def findSubstring(self, s, words):

        wlen, slen = len(words[0]), len(s)
        tlen = wlen * len(words)

        worddict = Counter(words)

        ans = []

        for offset in range(wlen):
            l, lmax = offset, slen - tlen

            while l <= lmax:
                tmp_idct = worddict.copy()
                match = True
                for r in range(l + tlen, l, -wlen):
                    word = s[r - wlen:r]
                    if word not in tmp_idct or tmp_idct[word] == 0:
                        match = False
                        break
                    tmp_idct[word] -= 1
                if match:
                    ans.append(l)
                l = r

        return ans


s = "barfoothefoobarman"
words = ["foo", "bar"]
"""
s = "barfoofoobarthefoobarman"
words = ["bar", "foo", "the"]
"""
s="wordgoodgoodgoodbestword"
words=["word","good","best","good"]
res = Solution().findSubstring(s, words)
print(res)
