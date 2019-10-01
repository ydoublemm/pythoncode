def log(func):
    def wrapper(*args,**kw):
        print('call %s()' % func.__name__)
        return func(*args,**kw)
    return wrapper


@log
def now():
    print('01点24分')

print(now.__name__)

now()




