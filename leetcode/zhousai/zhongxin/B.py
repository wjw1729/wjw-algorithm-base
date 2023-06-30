"""就两题？？？？？"""
from collections import Counter

sls=input().split()

cnt0=Counter(sls[0])
cnt1=Counter(sls[1])

for k,v in cnt1.items():
    if v-cnt0[k]==1:
        print(k)
        break