"""
author:wjw
分析：字典保存键值对，列表保存使用历史，capacity保存容量。
时间复杂度好像不是O(1)。
"""
class LRUCache:
    def __init__(self,capacity:int):
        self.capacity=capacity
        self.d={}
        self.his=[]


    def get(self,key:int):
        if key in self.d:
            self.his.remove(key)
            self.his.append(key)
            return self.d[key]
        else:
            return -1


    def put(self,key:int,value:int):
        if key in self.d:
            self.d[key]=value
            self.his.remove(key)
            self.his.append(key)
        else:
            if len(self.d)<self.capacity:
                self.d[key]=value
                self.his.append(key)
            else:
                self.d.pop(self.his[0])
                self.d[key]=value
                self.his.pop(0)
                self.his.append(key)

lRUCache=LRUCache(2)
lRUCache.put(1,1)
lRUCache.put(2,2)
lRUCache.get(1)
lRUCache.put(3,3)