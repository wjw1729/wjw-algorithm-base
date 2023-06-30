
t=int(input())

for _ in range(t):
    s=input()


    seq=''
    i=0
    find=False
    check=True
    for c in s:
        if not find and c not  in seq:
            seq+=c
        else:
            find=True
            if c==seq[i]:
                i += 1
                if i>=len(seq):
                    i=0

            else:
                check=False
                break

    if check:
        print('YES')
    else:
        print('NO')