def findMinAndMax(list):
    if(list == None):
        return None,None
    if(len(list) == 0):
        return None,None
    if(len(list) == 1):
        return list[0],list[0]
    return  min(list),max(list)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')