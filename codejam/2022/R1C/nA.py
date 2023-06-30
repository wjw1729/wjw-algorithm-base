


def nocanbuild(sls):

    adj=[0]*26
    for s in sls:
        if len(set(s))==1:
            continue

        l = 0
        while l<len(s):
            r=l+1
            while r<len(s) and s[r]==s[r-1]:
                r+=1
            if l!=0:
                adj[ord(s[l])-ord('A')]+=1
            if r!=len(s):
                adj[ord(s[l]) - ord('A')] += 1

    return any(x>2 for  x in sls)





