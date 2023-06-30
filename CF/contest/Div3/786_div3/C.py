

t=int(input())

for _ in range(t):
    s=input()
    st=input()

    if st=='a':
        print(1)
    elif 'a' in st:
        print(-1)
    else:
        times=s.count('a')
        print(2**times)