"""
开发者：林相希
开发日期 2021-10-19
内容：函数的高级用法-迭代
"""
#迭代数据字典中键的名字
D={"name":"zhangsan","age":20}
for key in D:
    print(key)
    
#迭代数据字典中的值
for value in D.values():
    print(value)

#迭代数据字典中的键和值
for key,value in D.items():
    print(key,value)