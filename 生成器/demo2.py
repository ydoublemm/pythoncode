def fib(n):
    count, a, b = 0, 0, 1
    while count < n:
        yield b
        a, b = b, a + b
        count += 1


# for i in fib(1000):
#     print(i)

# for n in fib(6):
#     print(n)

g = fib(6)

while True:
    try:
        n = next(g)
        print(n)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break