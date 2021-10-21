"""
开发者：林相希
开发日期 2021-10-21
内容：函数编程-reduce()-复合用法
"""

from functools import reduce


def tansint(x, y):
    return x * 10 + y


L = [5,2,0,1,2]
print(reduce(tansint, L))
