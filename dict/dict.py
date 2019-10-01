#相当与map,key是不可变对象
d = {'name':'ymm','age':18}
print(d['name'])

d.pop('name')
d['age'] = 19
print(d)
print('name' in d)