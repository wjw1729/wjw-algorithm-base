"""
做的有点复杂
"""

def bitflip(k,s):




    def dealeven(k,s):
        num1 = s.count('1')
        num0 = s.count('0')
        if k>num0 and num0%2==0:
            res='1'*n
            cnt1=[0 if s[i]=='1' else 1 for i in range(n)]
            cnt1[0]+=k-num0
            return res,cnt1

        elif k>num0:
            res='1'*(n-1)+'0'
            cnt1=[0 if s[i]=='1' else 1 for i in range(n)]
            cnt1[-1]+=k-num0
            return res,cnt1
        else:
            res=''
            cnt1=[0]*n
            for i in range(n):
                if s[i]=='1':
                    res+=s[i]
                else:
                    if k>0:
                        res+='1'
                        k -= 1
                        cnt1[i]=1
                    else:
                        res+='0'

            return res,cnt1
    if k%2==0:
        return  dealeven(k,s)


    else:
        ns=flip(s)

        res,cnt=dealeven(k-1,ns)
        res=list(res)
        check=False
        for i,c in enumerate(res):
            if c=='0':
                res[i]='1'
                cnt[i] += 1
                check=True
                break

        if not check:
            res=res[:-1]+['0']
            cnt[-1]+=1

        return ''.join(res),cnt



def flip(s):
    ns = ''
    for c in s:
        ns += '1' if c == '0' else '0'

    return ns






t=int(input())
for _ in range(t):
    n,k=[int(x) for x in input().split()]
    s=input()
    res,cnt1=bitflip(k,s)
    print(res)
    print(' '.join(str(x) for x in cnt1))

