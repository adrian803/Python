"""
开发者：林相希
开发日期 2021-10-12
内容：函数的定义和调用-循环和递归
"""


def sum_n(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
        return sum


print("本方法使用的是循环求和:", sum_n(100))


def sum_n_n_1(n):
    if n > 0:
        return n + sum_n_n_1(n - 1)
    else:
        return 0


print("本方法使用的是递归求和:", sum_n_n_1(100))
