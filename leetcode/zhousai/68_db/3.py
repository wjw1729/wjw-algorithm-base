class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False

        total=0
        stars=0

        for c,l in zip(s,locked):
            if l=='1':
                if c=='(':
                    total+=1
                else:
                    total-=1
                    if total<0 and stars>0:
                        total+=1
                        stars-=1
                    if total<0:
                        return False
            else:
                stars+=1

        total=0
        stars=0
        for c,l in zip(s,locked)[::-1]:
            if l=='1':
                if c==')':
                    total+=1
                else:
                    total-=1
                    if total<0 and stars>0:
                        total+=1
                        stars-=1
                    if total<0:
                        return False
            else:
                stars+=1

        return True