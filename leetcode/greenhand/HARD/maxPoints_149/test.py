def gcd(a, b):
    return gcd(b, a % b) if b != 0 else a


a = 6
b = 9
res = gcd(a, b)
print(res)
