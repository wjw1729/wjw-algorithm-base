from collections import Counter
import time
def judege(s):
    d=Counter(s)
    num=0
    for k,v in d.items():
        if v%2==1:
            num+=1
    if num>1:
        return False
    return True

def num(s):
    total=0
    n=len(s)
    for i in range(n-1,-1,-1):
        p=s[i:]
        if judege(p):
            total+=1

    return total


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        n=len(word)
        dp=[0]*(n+1)

        for i in range(1,n+1):

            dp[i]=dp[i-1]+num(word[:i])

        return dp[-1]

t1=time.time()
word = "aba"
word = "aabb"
word = "he"
word="ghffghcdigdgbfhaiejibbcidgfjahegedjecfhdjchdcaefeefiabebefjccdhdchacehfdjibcgcedjhhbadfgejhceghgjjegihhbfagciecdadhcjgdajgbhegjhicbifeefcaficcbcijciegihidacjahahjgdjdgfjcadgaiicgiiegaeifjbcjacefffgdgibjfijiiedcaahbceebheifbgffchdcfbbhfdfajggfhhhbhhgbcgfdgcfcdggihhcfcghbgbchcgaccccaabeejdhdbjicghddaaeedciigeeiehjhhhicajbddedidecjiebbggdehbgejabcbcjadicjgbabehbjjbehfegicabighbcahijjdcgehjhcbfheecgjdfbhadgbhfdefffbcbggifgdhdgahgejeegbadbifjdiaggdcjfaiigdjjehebjdabgdecfcebcfggceihffhjcjfaadhgeahiajjdghehieiidcfdjaeiehcjghjcajhgdhcfjcagiibhdiiabghcffaijehjjjiafjcgfjeghdbggbhfjdihahjedgdhhdibcdgaaafejgbdjgdfichbijjajicdfehafjbgdbieaecagdifeggbefegeajejbcfaidjbgbbgejjebidcdaeggcefjdfacachfeehajfabfhbcdjbcjdifiehdjghdhegfgababaeacdjcegffgdhadjehiebggdiececeiihfghcecahbhgefhihahhfhgdeaejgdhihcgfecgecebdjgcjicjdbcicigdbaehhjcdajbehdeahbibeejddajiacgchbcffagbbdiechcfgafehifibifhaidaeidjbeefefcaiejdhibebghbjgbbhchfjeefdfgjiijbbbgchgjhaefdgejfgeegbajgbcjejahgchfhjbgiiggjiaigiibccidcjcgbabed"
res=Solution().wonderfulSubstrings(word)
print(res)
print(time.time()-t1)