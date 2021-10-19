"""
开发者：林相希
开发日期 2021-10-7
内容：函数的定义和调用-可带多个参数进行处理(不固定参数个数)
"""


def fun_sum(*num):
    Sum = 0
    for n in num:
        Sum += n
    return Sum


print(fun_sum(1, 2, 3, 4, 5, 6))
