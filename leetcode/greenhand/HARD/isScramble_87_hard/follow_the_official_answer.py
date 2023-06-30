"""
跟着官方思路进行下去，
"""
import time

def f(s1, s2):
    if s1 == s2:
        return True

    n = len(s1)
    res = False
    for i in range(1, n):
        res = res or (f(s1[0:i], s2[0:i]) and f(s1[i:], s2[i:]))

    for i in range(1, n):
        res = res or (f(s1[0:i], s2[n - i:]) and f(s1[i:], s2[0:n - i]))
    return res

t1=time.time()
str1 = 'great'
str2 = 'rgeat'
str1='abcde'
str2='caebd'
str1="abcdefghijklmnopq"
str2="efghijklmnopqcadb"
result = f(str1, str2)
print(result)
print(time.time()-t1)
