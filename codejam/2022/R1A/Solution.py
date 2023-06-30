def main():
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        A1 = [2**i for i in range(30)]
        A2 = [10**9-i for i in range(N-30)]
        A = A1+A2

        print(*A, flush=True)

        *B, = map(int, input().split())

        s = sum(A) + sum(B)

        x = []
        for i in B+A2:
            if 2*(sum(x) + i) <= s:
                x.append(i)

        for i in A1[::-1]:
            if 2*(sum(x)+i) <= s:
                x.append(i)

        assert(sum(x)*2 == s)

        print(*x, flush=True)


if __name__ == '__main__':
    main()
