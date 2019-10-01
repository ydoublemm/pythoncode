def odd(n):
    return n%2

x = filter(odd,[1,2,3,4,5,6])

print(list(x))


def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n

def _not_divisible(n):
    return lambda x:x%n>0

def prime():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible,it)


# 打印1000以内的素数:
for n in prime():
    if n < 1000:
        print(n)
    else:
        break