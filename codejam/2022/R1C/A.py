from collections import defaultdict


def nocanbuild(sls):
    adj = [0] * 26
    for s in sls:
        if len(set(s)) == 1:
            continue

        l = 0
        while l < len(s):
            r = l + 1
            while r < len(s) and s[r] == s[r - 1]:
                r += 1
            if l != 0:
                adj[ord(s[l]) - ord('A')] += 1
            if r != len(s):
                adj[ord(s[l]) - ord('A')] += 1

            l=r

    return any(x > 2 for x in adj)

def buildtower(sls):
    if nocanbuild(sls):
        return 'IMPOSSIBLE'


    hd=defaultdict(list)
    ed=defaultdict(list)
    deg=[0]*26
    contls=['' for _ in range(26)]

    cnt=0
    for s in sls:
        if len(s)>0 and s[0]==s[-1] and len(set(s))!=1:
            return 'IMPOSSIBLE'
        if len(set(s))==1:
            contls[ord(s[0])-ord('A')]+=s
        else:

            hd[s[0]].append(s)
            cnt+=1
            ed[s[-1]].append(s)
            deg[ord(s[0])-ord('A')]+=1
            deg[ord(s[-1]) - ord('A')] += 1

    if any(len(x)>1 for x in hd.values()) or any(len(x)>1 for x in ed.values()) or not( (sum(x==1 for x in deg)==2 and hd) or (sum(x==1 for x in deg)==0  and not hd)):
        return 'IMPOSSIBLE'

    ans=''
    for i in range(26):
        if deg[i]==1 and chr(ord('A')+i) in hd:
            ans+=hd[chr(ord('A')+i)][0]
            cnt-=1
            break
    if ans and contls[ord(ans[0]) - ord('A')] != '':
        ans=contls[ord(ans[0]) - ord('A')]+ans
        contls[ord(ans[0]) - ord('A')]=''

    if ans and contls[ord(ans[-1]) - ord('A')] != '':
        ans += contls[ord(ans[-1]) - ord('A')]
        contls[ord(ans[-1]) - ord('A')] = ''

    while ans and  cnt>0 :
        ans+=hd[ans[-1]][0]
        cnt-=1

        if  contls[ord(ans[-1])-ord('A')]!='':
            ans+=contls[ord(ans[-1])-ord('A')]
            contls[ord(ans[-1]) - ord('A')]=''

    if all(x=='' for x in contls):
        return ans
    else:
        ans+=''.join(contls)
        return ans





t=int(input())


for i in range(t):
    n=int(input())
    sls=input().split(' ')
    res=buildtower(sls)
    print('Case #%d: %s'%(i+1,res))




