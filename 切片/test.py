# def trim(str):
#
#     count1 = 0
#     count2 = 0
#
#     for i in str:
#         if i == ' ':
#             count1 += 1
#         else:
#             break;
#
#     for i in reversed(str):
#         if i == ' ':
#             count2 += 1
#         else:
#             break;
#
#     str = str[count1:len(str)]
#     str = str[0:len(str)-count2]
#
#     return str

def trim(str):
    while str[:1] == ' ':
        str = str[1:]
    while str[-1:] == ' ':
        str = str[:-1]

    return str

    # 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')