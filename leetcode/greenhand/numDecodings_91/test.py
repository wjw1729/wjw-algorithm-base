s='10000110101010'
ls=list(s)
while '0' in ls:
    ls.remove('0')
ls=''.join(ls)
print(ls)
