"""
author:wjw
分析：耐心分析就好了。耐心调试。
"""


class Solution:
    def fullJustify(self, words, maxWidth):
        ans = []
        n = len(words)
        i = 0
        while i < n:
            tmp_word_ls = []
            length = 0
            j = 0
            if i==6:
                print(1)

            while i + j < n and length + len(words[i + j]) <= maxWidth:
                tmp_word_ls.append(words[i + j])
                length += len(words[i + j]) + 1
                j += 1

            if i + j == n:
                ans.append(' '.join(tmp_word_ls).ljust(maxWidth))
                break

            if len(tmp_word_ls) == 1:
                ans.append(tmp_word_ls[0].ljust(maxWidth))

            else:
                stripnum = maxWidth - sum([len(x) for x in tmp_word_ls])

                while stripnum > 0:
                    for k in range(len(tmp_word_ls) - 1):
                        if stripnum <= 0:
                            break
                        tmp_word_ls[k] += ' '
                        stripnum -= 1
                ans.append(''.join(tmp_word_ls))
            i = i + j

        return ans


words = ["This", "is", "an", "example", "of", "text", "justification."]
#words = ["What", "must", "be", "acknowledgment", "shall", "be"]
#words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 16
res = Solution().fullJustify(words, maxWidth)
print(res)
