

t=int(input())

for _ in range(t):
    s=input()

    def solve(s):
        n=len(s)
        s=list(s)

        l=n//2-s.count('(')
        r=n//2-s.count(')')

        ns=False
        c=0
        for i in range(n):
            if s[i]=='(':
                c+=1
            elif s[i]==')':
                c-=1
            else:
                if l==0:
                    return True

                elif r==0:
                    return True

                else:
                    if not ns and c==0:
                        s[i]='('
                        l-=1
                        c+=1
                    else:
                        ns=True

        ns=False
        for i in range(n-1,-1,-1):
            if s[i]==')':
                c+=1
            elif s[i]=='(':
                c-=1
            else:
                if l==0 or r==0:
                    return True

                else:
                    if not ns and c==0:
                        s[i]=')'
                        r-=1
                        c+=1
                    else:
                        ns=True

        return l==0 or r==0

    if solve(s):
        print('YES')
    else:
        print('NO')











