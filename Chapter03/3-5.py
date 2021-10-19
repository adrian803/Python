"""
开发者：林相希
开发日期 2021-10-7
内容：函数的定义和调用-带参数进行处理(不固定参数个数)-参数带默认值
"""


def personinfo(name, age, gander='female'):
    print(name, age, gander)


personinfo('张三', 44, 'male')

personinfo('tony', 18)
