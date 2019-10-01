def log(text):
    def decorator(func):
        def warpper(*args,**kw):
            print("%s %s()" % (text,func.__name__))
            return func(*args,**kw)
        return warpper
    return  decorator




@log("111")
def now():
    print('01点24分')


now = log('execute')(now)
print(now.__name__)

now()
