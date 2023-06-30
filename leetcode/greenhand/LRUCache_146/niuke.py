"""
牛客网
author:wjw
分析：要自己写输入输出格式转换的。
"""
class DLinkNode:
    def __init__(self, key=0, value=0, pre=None, next=None):
        self.key = key
        self.value = value
        self.pre = pre
        self.next = next


class LRU:
    # write code here
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = DLinkNode()
        self.tail = DLinkNode()
        self.size = 0
        self.head.next = self.tail
        self.tail.pre = self.head

    def addToHead(self, node):
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node
        node.pre = self.head

    def moveToHead(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        self.addToHead(node)

    def removeNode(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def removeTail(self):
        self.tail.pre = self.tail.pre.pre
        self.tail.pre.next = self.tail

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.moveToHead(node)
            return node.value
        else:
            return -1

    def set(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)
        else:
            if self.size < self.capacity:
                node = DLinkNode(key, value)
                self.cache[key] = node
                self.addToHead(node)
                self.size += 1
            else:
                self.cache.pop(self.tail.pre.key)
                self.removeTail()
                node = DLinkNode(key, value)
                self.cache[key]=node
                self.addToHead(node)


input='[[1,-324690837,-72487934],[1,-723504364,-369145172],[2,-324690837],[1,724101438,-30727452],[1,366967562,290286156],[2,366967562],[1,-21417066,-450706222],[1,-484359960,-121414361],[1,-629538923,-759874959],[1,-461538894,749719150],[1,-338664886,-3080586],[2,522415046],[1,134352387,-391032350],[1,283492390,210901529],[2,-328994470],[2,-254674447],[2,85161833],[1,36899859,-561167545],[1,-232060336,889831435],[1,-848557701,-189598178],[2,-81051921],[1,57162090,-193776405],[1,157908494,-941008658],[2,-21417066],[2,-485579587],[2,449908952],[1,12002448,-273547528],[1,-267371849,634867878],[1,128963067,102756157],[2,36899859],[2,145140817],[2,335181121],[1,89294557,-213039610],[2,204879021],[2,36899859],[2,-371773103],[1,-354568989,-788098655],[2,283492390],[2,148848181],[1,641416456,-646693824],[1,-970438681,341383327],[1,452656493,-68334619],[1,209021588,229415889],[1,580338695,-286744639],[1,263639066,-99669610],[1,-586507345,255143085],[2,89294557],[2,209021588],[1,888670782,-378802985],[1,-751520980,8161338],[2,12002448],[1,-967501590,-351688503],[2,514432065],[2,80361112],[1,220830017,-93263524],[2,32131049],[1,-264084048,-155050456],[1,-482193643,-232757642],[2,134352387],[1,-303458351,-974058471],[2,452656493],[1,505909889,-508809796],[1,28202319,577206570],[2,-991605984],[2,-266360965],[2,553306411],[1,-91084058,95483640],[1,141869753,-629556641],[1,-48119420,783684131],[1,610948343,6884450],[2,641416456],[1,-412360441,31222570],[1,431900251,231767188],[2,-588592923],[1,-220001478,-183147041],[2,-69417139],[2,-34241947],[1,396626603,-435781001],[2,161660462],[2,-788025808],[2,-622427224],[1,-18852505,647730929],[2,-978490],[1,-203099668,-173289604],[1,-9216750,-116999009],[2,241113210],[2,-586507345],[1,439742836,3892905],[1,362692206,64119965],[1,-343557119,25898321],[1,351163245,558921656],[2,220830017],[2,-139705440],[1,-63307654,582782467],[1,174271875,647087188],[1,-366938003,141242360],[2,225133310],[2,-49488568],[2,-303458351],[2,505909889],[2,-808960104]],3'
s = input.strip()
a = s.split(']],')
k = int(a[1])
ops = a[0].strip("[[").split('],[')
s = LRU(k)
res = []
for op in ops:
    temp = op.split(',')
    if temp[0] == '1':
        s.set(temp[1], int(temp[2]))
    else:
        res.append(s.get(temp[1]))
print(str(res).replace(' ', ''))




