import time


def get_mod(a, b, c):
    res = 1
    temp = a
    while b > 0:
        if b & 1:
            res = (res * temp) % c
        temp = (temp * temp) % c
        b >>= 1
    return res


a = 5
b = 1564646464646645466999999999999999999999464646497974676457567567649759747947
c = 10 ** 9 + 7
t1 = time.time()
for i in range(100):
    print(get_mod(a, b, c))
print(time.time() - t1)
t2 = time.time()
for i in range(100):
    print(pow(a, b, c))
print(time.time() - t2)
