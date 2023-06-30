from collections import Counter


def isPart(A, B):
    d1 = Counter(B)
    d2 = Counter(A)
    for k, v in d1.items():
        if v <= d2[k]:
            continue
        else:
            return False
    return True


B = 'ceop'
A = 'facebook'
result = isPart(A, B)
print(result)
