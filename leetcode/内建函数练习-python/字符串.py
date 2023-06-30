"""
字符串的一些内建函数
40个。

"""

#1.capitalize()。大写
s='abc'
s=s.capitalize()
print(s)

#2.center().居中填充，用指定字符
s='abc'
s=s.center(8,'#')
print(s)

#3.左对齐填充。
s='abc'
s=s.ljust(8,'#')
print(s)

#4.右对齐填充.
s='abc'
s=s.rjust(8,'#')
print(s)

#??.用0填充，右对齐。
s='abc'
print(s.zfill(8))

#3.count().字符串计数，指定起始和结束范围。
s='aaaaaa'
print(s.count('aa'))

#4.编码.指定编码方法
s='aaa'
print(s.encode('UTF-8'))

#5.解码。
print(s.encode('UTF-8').decode('UTF-8'))

#6.判断是否以字符为结尾。可指定起始和结束范围。
s='abc'
print(s.endswith('c'))

#??.判断是否以字符为开头。可指定起始和结束范围。
s='abc'
print(s.startswith('a'))

#7.将字符串中的tab(制表符)转为空格。(默认为8)
s='ab\tc'
s=s.expandtabs()
print(s)

#8.查找是否包含指定字符串。可指定起始和结束范围。（不在，返回-1，在返回起始索引值）
s='abcdefg'
print(s.find('bc'))
print(s.find('z'))

#9.同上。（只是不在，会返回异常）
s='abcdefg'
print(s.index('bc'))
#print(s.index('z'))

#??.从右边开始寻找.可指定起始和结束范围.
s='abbba'
print(s.rfind('a'))

#??.从右边开始寻找。可指定起始和结束范围.
s='abbba'
print(s.rindex('a'))

#10.至少有一个字符且所有字符都是字母或数字。
s='abc123'
print(s.isalnum())
print(''.isalnum())
print('#'.isalnum())

#11.至少有一个字符且所有字符都是字母或中文。
s='abcd你好嘛'
print(s.isalpha())

#12.只包含数字.
s='12345'
print(s.isdigit())
print(''.isdigit())

#13.只包含数字字符。
s='12345'
print(s.isnumeric())
print(''.isnumeric())

#14.是否只包含十进制字符串.
s='123'
print(s.isdecimal())

#15.包含至少一个区分大小写的字符，且都是小写。
s='123b'
print(s.islower())

#16.包含至少一个区分大小写的字符，且都是大写。
s='123B'
print(s.isupper())

#??.转为小写。
s='ABC123'
print(s.lower())

#??.转为大写.
s='abc123'
print(s.upper())

#??.转换大小写。
s='abcABC'
print(s.swapcase())

#17.只包含空白
s='   '
print(s.isspace())

#18.是标题化的。(每个词首字母大写)
s='This Is A Title.'
print(s.istitle())

#??.字符串标题化
s='this is a title.'
print(s.title())

#19.连接。
sls=['a','b','c']
print(''.join(sls))
print(''.join(set(sls)))

#20.字符串长度.
s='abcdefg'
print(len(s))

#??.截取左右边空格或指定字符.
s='   abc   '
print(s.strip())

#??.截除左边空格或指定字符.
s='   abc'
print(s.lstrip())

#??.截除右边空格或者指定字符.
s='abc   '
print(s.rstrip())

#??.创建字符映射的转换表.
s1='aeiou'
s2='12345'
s='this is string example wow!!'
trans=str.maketrans(s1,s2)

#??.转换
print(str.translate(s,trans))

#??.返回字符串中最大的字母。
s='abcdefg'
print(max(s))

#??.返回字符串中最小的字母.
s='abcdefg'
print(min(s))

#??.替换。可以指定替换最大次数
s='aaaa'
print(s.replace('aa','b',1))

#??.以指定字符作为分隔符分割字符。可指定个数
s='a b c'
print(s.split(' ',1))

#??.换行分割.(可不换行?????????????)
s='a\rb\r\nc\nd'
print(s.splitlines(keepends=False))

#



