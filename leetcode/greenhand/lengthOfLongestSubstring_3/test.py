"""
author:wjw
usage:测试bug专用
"""

l=[1,2,3,4,5,6]
idx=l.index(5)
l=l[idx+1:].append(3)
print(l)