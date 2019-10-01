import sys
sys.setrecursionlimit(100000000)

def fact1(a):
    if a==1:
        return a
    else:
        return a+fact1(a-1)

print(fact1(1000))


def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact(1099))


def move(n, a='A', b='B', c='C'):
    if n==1:
        print(a,'-->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)

move(3)