class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        dls = list(dominoes)
        n = len(dls)
        power = []
        for i in range(n):
            if i > 0 and dls[i] == 'L' and dls[i - 1] == '.':
                power.append(i)

            if i < n - 1 and dls[i] == 'R' and dls[i + 1] == '.':
                power.append(i)

        while power:
            tmp = []

            for idx in power:
                if dls[idx] == 'L':
                    if dls[idx - 1] == 'R':
                        dls[idx - 1] = '.'
                    else:
                        dls[idx - 1] = 'L'
                        if idx - 2 >= 0 and dls[idx - 2] == '.':
                            tmp.append(idx - 1)

                elif dls[idx] == 'R':
                    if dls[idx + 1] == 'L':
                        dls[idx + 1] = '.'
                    else:
                        dls[idx + 1] = 'R'
                        if idx + 2 < n and dls[idx + 2] == '.':
                            tmp.append(idx + 1)

            power=[]
            for i in tmp:
                if i > 0 and dls[i] == 'L' and dls[i - 1] == '.':
                    power.append(i)

                if i < n - 1 and dls[i] == 'R' and dls[i + 1] == '.':
                    power.append(i)

        return ''.join(dls)

dominoes = ".L.R...LR..L.."
res=Solution().pushDominoes(dominoes)
print(res)