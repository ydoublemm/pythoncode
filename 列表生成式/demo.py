import os


print(
    [x for x in range(1,11)],'\n',
    [x*x for x in range(1,11)] ,'\n',
    [x*x for x in range(1,11) if x%10 ==0] ,'\n',
    [m+n for m in 'abc' for n in 'ABc'],'\n',
    [d for d in os.listdir('../')],'\n',
    [s.lower() for s in ['a','b','c']]
)
