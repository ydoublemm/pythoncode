high = 1.75
weight = 80.5
bmi = weight / (high*high)
if(bmi < 18.5):
    print('过轻')
elif(18.5 <bmi < 25):
    print('正常')
elif(25<bmi<32):
    print('肥胖')
else:
    print('过度肥胖')