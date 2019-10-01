def my_max(a,b):
    return a if a>b else b


print('a'<'b')


def my_abs(a):
    return a if a>0 else -a


print(my_abs(-9))


def my_sum(a):
    t=[]
    for i in range(a+1):
        for j in range(a+1):
            if(i+j == a):
                t.append(i)
                t.append(j)

    return t

# for i in range(len(my_sum(100))):
#     print(my_sum(100)[i])
#     print( my_sum(100)[i+1])
#     i+=2

def my_pow(x,n=2):
    return x if x <=1 else pow(x,n)

print(my_pow(8,3))



