"""
author:off
分析：他们也太牛了，我还是太菜了，难顶！
"""

import time
from collections import Counter
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        freq = Counter([0])
        mask, ans = 0, 0

        for ch in word:
            idx = ord(ch) - ord("a")
            mask ^= (1 << idx)
            if mask in freq:
                ans += freq[mask]
            for i in range(10):
                mask_pre = mask ^ (1 << i)
                if mask_pre  in freq:
                    ans += freq[mask_pre]
            freq[mask] += 1

        return ans


t1=time.time()
word = "aba"
word = "aabb"
word = "he"
word="ghffghcdigdgbfhaiejibbcidgfjahegedjecfhdjchdcaefeefiabebefjccdhdchacehfdjibcgcedjhhbadfgejhceghgjjegihhbfagciecdadhcjgdajgbhegjhicbifeefcaficcbcijciegihidacjahahjgdjdgfjcadgaiicgiiegaeifjbcjacefffgdgibjfijiiedcaahbceebheifbgffchdcfbbhfdfajggfhhhbhhgbcgfdgcfcdggihhcfcghbgbchcgaccccaabeejdhdbjicghddaaeedciigeeiehjhhhicajbddedidecjiebbggdehbgejabcbcjadicjgbabehbjjbehfegicabighbcahijjdcgehjhcbfheecgjdfbhadgbhfdefffbcbggifgdhdgahgejeegbadbifjdiaggdcjfaiigdjjehebjdabgdecfcebcfggceihffhjcjfaadhgeahiajjdghehieiidcfdjaeiehcjghjcajhgdhcfjcagiibhdiiabghcffaijehjjjiafjcgfjeghdbggbhfjdihahjedgdhhdibcdgaaafejgbdjgdfichbijjajicdfehafjbgdbieaecagdifeggbefegeajejbcfaidjbgbbgejjebidcdaeggcefjdfacachfeehajfabfhbcdjbcjdifiehdjghdhegfgababaeacdjcegffgdhadjehiebggdiececeiihfghcecahbhgefhihahhfhgdeaejgdhihcgfecgecebdjgcjicjdbcicigdbaehhjcdajbehdeahbibeejddajiacgchbcffagbbdiechcfgafehifibifhaidaeidjbeefefcaiejdhibebghbjgbbhchfjeefdfgjiijbbbgchgjhaefdgejfgeegbajgbcjejahgchfhjbgiiggjiaigiibccidcjcgbabed"
res=Solution().wonderfulSubstrings(word)
print(res)
print(time.time()-t1)