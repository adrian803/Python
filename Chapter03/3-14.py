"""
开发者：林相希
开发日期 2021-10-19
内容：函数高级用法——表达式生成器
"""
#列表生成
print([x*x for x in range(1,1000)])
print([7*x for x in range(1,1000)])

#对象生成
Obj =(x*x for x in range(1,10))
for i in Obj:
    print(i)