from collections import Counter

words = ["i", "love", "leetcode", "i", "love", "coding"]
d = Counter(words)
d1 = {}
for k, v in d.items():
    if v not in d1.keys():
        d1[v] = [k]
        continue
    d1[v].append(k)

print(1)
