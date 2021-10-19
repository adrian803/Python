"""
开发者：林相希
开发日期 2021-10-12
内容：函数的定义和调用-无参数
"""


def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n - 1) * n


print("100的阶乘是：", fact(100))
