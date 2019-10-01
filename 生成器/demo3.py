def odd():
    print('step1')
    yield 2
    print('step2')
    yield 3
    print('step3')
    yield 5

o = odd()
x1= next(o)
print(x1)
next(o)
next(o)
next(o)
