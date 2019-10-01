chars = ['a','b','c'];

print(len(chars))
print(chars[0])
print(chars[-1])
#在最后添加元素
chars.append('d')
print(len(chars))

#在索引为1的位置插入元素,插入后该元素的索引编程1
chars.insert(1,'0');
print(chars[1])

#删除索引在-1的元素
chars.pop()
chars.pop(-1)
print(chars)

chars[1] = '1'
print(chars)


