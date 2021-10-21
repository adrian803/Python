"""
开发者：林相希
开发日期 2021-10-21
内容：函数编程-map（）
"""

def f(x):
    return x * x


L = map(f, [1, 3, 5,7,9])
f_map = map(f,L)
print(list(f_map))