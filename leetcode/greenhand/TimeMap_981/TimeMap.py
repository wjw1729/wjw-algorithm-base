"""
author:wjw
分析：
"""

import bisect


class TimeMap:
    def __init__(self):
        self.d = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d.setdefault(key, [])
        self.d[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ''
        if timestamp >= self.d[key][-1][1]:
            return self.d[key][-1][0]

        tim_obj = [x[1] for x in self.d[key]]
        index = bisect.bisect(tim_obj, timestamp)
        if index != 0:
            return self.d[key][index - 1][0]
        else:
            return ''


kv = TimeMap()
kv.set('foo', 'bar', 1)
res = kv.get('foo', 1)
print(res)
