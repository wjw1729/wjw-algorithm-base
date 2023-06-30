


t=int(input())

for _ in range(t):
    score=int(input())
    if score<1400:
        print('Division 4')
    elif score<1600:
        print('Division 3')
    elif score<1900:
        print('Division 2')
    else:
        print('Division 1')