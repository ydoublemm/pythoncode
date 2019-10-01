a = [1,2,3]

def sum(*num):
    s = 0
    for i in num:
        s+=i
    return s

print(sum(1,2,3,4,5,6))
print(max(*a))


def my_kw(**kw):
    print(kw)

print(my_kw(**{'name':'ymm','age':18}))

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Bob', 35, city='Beijing')


def person(name, age, *, city, job):
    print(name, age, city, job)

person('ymm',18,city='ningbo',job='程序员')

def person(name, age, *args, city, job):
    print(name, age, args, city, job)

person('ymm',18,city='ningbo',job='程序员')



