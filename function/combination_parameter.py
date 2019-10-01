#组合参数

def f1(a,b=0,*args,**kw):
    print('a=',a,'b=',b,'args=',args,'kw=',kw)

f1(1)
f1(1,2)
f1(1,2,1,2,3)
f1(1,2,1,2,3,si='4',wu=5)

print('-----------------')

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f2(1,2,d=99)
f2(1,2,3,d=99)
f2(1,2,3,d=99,si='4',wu=5)