"""
开发者：林相希
开发日期 2021-10-19
内容：函数高级用法——表达式生成器yield
"""

def count_n(n):
    while n>0:
        yield n
        n-=1

for i in count_n(10):
    print(i)