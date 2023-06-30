"""
author:wjw
"""


def transaction(transaction):
    name, time, amount, city = transaction.split(',')
    return (name, time, amount, city)


class Solution:
    def invalidTransactions(self, transactions):
        res = []
        isok = [False] * len(transactions)

        for i in range(len(transactions)):
            name1, time1, amount1, city1 = transaction(transactions[i])

            if int(amount1) > 1000:
                if isok[i] == False:
                    res.append(transactions[i])
                    isok[i] = True

            for j in range(i + 1, len(transactions)):
                name2, time2, amount2, city2 = transaction(transactions[j])

                if name1 == name2 and city1 != city2 and abs(int(time1) - int(time2)) <= 60:
                    if isok[i] == False:
                        res.append(transactions[i])
                        isok[i] = True
                    if isok[j] == False:
                        res.append(transactions[j])
                        isok[j] = True

        return res


transactionstransactions = ["bob,689,1910,barcelona", "alex,696,122,bangkok", "bob,832,1726,barcelona",
                            "bob,820,596,bangkok", "chalicefy,217,669,barcelona", "bob,175,221,amsterdam"]
result = Solution().invalidTransactions(transactionstransactions)
print(result)
