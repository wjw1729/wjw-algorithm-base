
def parse_a_b_c(s):


    b=0
    op=[]
    pre=None
    for i in range(len(s)):
        if s[i]=='(':
            b+=1
        if s[i]==')':
            b-=1

        if  b==0 and (s[i]==' ' or i==len(s)-1):
            if pre!=None :
                if s[i]==' ':
                    op.append(s[pre+1:i])
                else:
                    op.append(s[pre+1:i+1])
            pre=i

    return op


inp='mult x (let x 3 y 4 (add x y))'
res=parse_a_b_c(inp)
print(res)
