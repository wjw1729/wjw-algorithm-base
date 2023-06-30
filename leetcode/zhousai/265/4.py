
class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:

        def my_split(s):
            res=[]
            n=len(s)
            l=0
            r=0
            while l<n:
                while r<n and s[r].isdigit() == s[l].isdigit() :
                    r+=1
                res.append(s[l:r])
                l=r

            return res

        def splitnum(num):
            n=len(num)
            if n==1:
                return [[num]]
            if n==2:
                return [[num],[num[0],num[1]]]
            if n==3:
                return [[num],[num[0],num[1],num[2]],[num[0],num[1:]],[num[0:-1],num[-1]]]

        def filling(slist):
            return ''.join([ x if x.isalpha() else '*'*int(x)  for x in slist])

        def my_len(slist):
            return sum(len(x) if x.isalpha() else int(x) for x in slist)
        def canbe(a):
            a=my_split(a)

            a_part=[]
            for x in a:
                if x.isalpha():
                    a_part.append([[x]])#加上[]
                else:
                    a_part.append(splitnum(x))

            n=len(a_part)

            a_res=[[]]
            for i in range(n):
                a_res=[x+y for x in a_res for y in a_part[i]]


            return a_res

        s1_list=canbe(s1)
        s2_list=canbe(s2)

        pairs=[]
        for a in s1_list:
            for b in s2_list:
                print(my_len(a),my_len(b))
                if my_len(a)==my_len(b):
                    pairs.append((a,b))

        for a,b in pairs:
            a_original=filling(a)
            b_original=filling(b)
            check=True
            for i in range(len(a_original)):
                if a_original[i]==b_original[i] or a_original[i]=='*' or b_original[i]=='*':
                    continue

                check=False
            if check:
                return True




        return False


s1 = "l123e"
s2 = "44"
s1 = "internationalization"
s2 = "i18n"

s1="v816u32v813u84v4v12u393v877"
s2="586v993u497u836u9v59v83u34v8"
res=Solution().possiblyEquals(s1,s2)
print(res)





