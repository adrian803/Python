"""
开发者：林相希
开发日期 2021-10-21
内容：函数编程-reduce()
"""

from functools import reduce


def addnum(x, y):
    return x + y


print(reduce(addnum, range(1, 101)))

