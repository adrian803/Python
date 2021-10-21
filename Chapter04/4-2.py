"""
开发者：林相希
开发日期 2021-10-21
内容：函数编程-map()应用
"""
def format_name(SName):
    s_fname=SName[0:1].upper()+SName[1:].lower()
    return s_fname


L=["lISa","TOmI","MArrY"]
r_tname=map(format_name,L)
print(list(r_tname))


def format_name2(SName1):
    s_fname=SName1[:].upper()
    return s_fname


r_tname2=map(format_name2,L)
print(list(r_tname2))


def format_name3(SName2):
    s_fname=SName2[:].lower()
    return s_fname


r_tname3=map(format_name3,L)
print(list(r_tname3))


def format_name4(SName3):
    s_fname="S_"+SName3[:].lower()
    return s_fname


r_tname4=map(format_name4,L)
print(list(r_tname4))