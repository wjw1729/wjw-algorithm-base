import math
chosels=[]
for i in range(41):
    chosels.append(2**i)
for j in range(3,20):
    if math.factorial(j)>10**12:
        break
    chosels.append(math.factorial(j))



chosels.sort()

def minpossb(n):


    def cansplit(k)if
:

