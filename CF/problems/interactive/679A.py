


primes=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,4,9,25,49]
cnt=0

for i in range(19):
    print(primes[i],flush=True)
    if input()=='yes':
        cnt+=1

    if cnt>=2:
        break

if cnt>=2:
    print('composite',flush=True)
else:
    print('prime',flush=False)


