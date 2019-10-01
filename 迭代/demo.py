from collections import  Iterable

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)

for key,value in d.items():
    print(key,value)

for i,value in enumerate(range(10)):
    print(i,value)

for value in 'abc':
    print(value)


print(isinstance('abc',Iterable))