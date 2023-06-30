

from collections import Counter
def count(B):
    d=Counter(B[0])
    for i in range(len(B)):
        d1=Counter(B[i])
        for k,v in d1.items():
            if v>d[k]:
                d[k]=v
    return d



B = ["ec","oc","ceo"]

res=count(B)
print(res)
