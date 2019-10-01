def clca_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax +=n
        return ax
    return sum

f=clca_sum(1,2,3,4)
print(f())


def count():
    fs = []
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs

f1,f2,f3 = count()
print(f1(),f2(),f3())


def count2():
    def square(j):
        return lambda : j*j
        return sq
    fs = []
    for i in range(1,4):
        fs.append(square(i))
    return fs

f4,f5,f6 = count2()
print(f4(),f5(),f6())

