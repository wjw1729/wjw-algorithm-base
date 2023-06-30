
class Solution:
    def checkZeroOnes(self, s: str) -> bool:

        if s=='1':
            return True
        if s=='0':
            return False
        length0 = 0
        length1 = 0

        n = len(s)
        pre = s[0]
        length = 1

        for i in range(1, n):

            if s[i] == pre:
                length += 1

            if  s[i] != pre:
                if pre == '1':
                    length1 = max(length1, length)
                else:
                    length0 = max(length0, length)

                length = 1

            if i==n-1:
                if s[i]==pre=='1':
                    length1=max(length1,length)
                if s[i]==pre=='0':
                    length0=max(length0,length)
                if s[i]!=pre:
                    if s[i]=='1':
                        length1=max(length1,1)
                    else:
                        length0=max(length0,1)

            pre = s[i]
        return length1 > length0

s = "1101"
s = "111000"
s = "110100010"
s='10'
res=Solution().checkZeroOnes(s)
print(res)