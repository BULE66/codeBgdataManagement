# _author:kate.wei
# date:2021/3/28
'''
总结：
1. 算数优先级大于比较运算符
2. 比较运算符优先级大于逻辑运算符
3. 逻辑运算符内部三个优先级 not >and > or
'''

print(1+1 > 2+2)  # 2>4
print(1>2 and 2>3)  # False and False
print(not (1>2)or 2>3 and 10<3) # not False or False and False
# True or False and False
# True or False
