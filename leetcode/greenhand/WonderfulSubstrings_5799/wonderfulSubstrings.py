"""
author；wjw
分析：状态压缩+哈希表（字典）.mask为一个10位的状态用于存放当前前缀下jihgfedcba对应的奇偶性。00000000000表示初始状态，出现次数记为1。便于找到同奇同偶的状态，则两次状态之间的字符串为最美字符串。
"""

from collections import Counter


class Solution:
    def wonderfulSubstrings(self, word):
        freq = Counter([0])
        mask, ans = 0, 0

        for ch in word:
            index = ord(ch) - ord("a")
            mask = mask ^ (1 << index)
            if mask in freq:
                ans += freq[mask]
            for i in range(10):
                mask_pre = mask ^ (1 << i)
                if mask_pre in freq:
                    ans += freq[mask_pre]
            freq[mask] += 1

        return ans


word = "aba"
word = "aabb"
word = "he"
word = "ghffghcdigdgbfhaiejibbcidgfjahegedjecfhdjchdcaefeefiabebefjccdhdchacehfdjibcgcedjhhbadfgejhceghgjjegihhbfagciecdadhcjgdajgbhegjhicbifeefcaficcbcijciegihidacjahahjgdjdgfjcadgaiicgiiegaeifjbcjacefffgdgibjfijiiedcaahbceebheifbgffchdcfbbhfdfajggfhhhbhhgbcgfdgcfcdggihhcfcghbgbchcgaccccaabeejdhdbjicghddaaeedciigeeiehjhhhicajbddedidecjiebbggdehbgejabcbcjadicjgbabehbjjbehfegicabighbcahijjdcgehjhcbfheecgjdfbhadgbhfdefffbcbggifgdhdgahgejeegbadbifjdiaggdcjfaiigdjjehebjdabgdecfcebcfggceihffhjcjfaadhgeahiajjdghehieiidcfdjaeiehcjghjcajhgdhcfjcagiibhdiiabghcffaijehjjjiafjcgfjeghdbggbhfjdihahjedgdhhdibcdgaaafejgbdjgdfichbijjajicdfehafjbgdbieaecagdifeggbefegeajejbcfaidjbgbbgejjebidcdaeggcefjdfacachfeehajfabfhbcdjbcjdifiehdjghdhegfgababaeacdjcegffgdhadjehiebggdiececeiihfghcecahbhgefhihahhfhgdeaejgdhihcgfecgecebdjgcjicjdbcicigdbaehhjcdajbehdeahbibeejddajiacgchbcffagbbdiechcfgafehifibifhaidaeidjbeefefcaiejdhibebghbjgbbhchfjeefdfgjiijbbbgchgjhaefdgejfgeegbajgbcjejahgchfhjbgiiggjiaigiibccidcjcgbabed"
res = Solution().wonderfulSubstrings(word)
print(res)
