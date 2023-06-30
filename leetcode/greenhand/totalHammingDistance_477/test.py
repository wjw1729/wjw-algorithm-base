nums = [4, 14, 2]
str_nums = map("{:032b}".format, nums)
str_nums_bits = zip(*str_nums)
c=list(str_nums_bits)
sum = 0
for b in str_nums_bits:
    sum += b.count('0') * b.count('1')
print(sum)