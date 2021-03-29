# _author:kate.wei
# date:2021/3/28
'''
变量的赋值方式
变量是一个容器（内存地址），存储数据

方式1：单个变量赋值
id():查看变量的内存地址
内存分配
方式2：连续赋值
方式3： 连续赋值，不同变量的不一样的初始值
注意点：变量的个数要与值的个数一直，否则会报错

'''
# age1 = 18
# age2 = 18
# age3 = 18
# print(age1,age2,age3,id(age1),id(age2),id(age3))

age1=age2=age3=18
print(age1,age2,age3,id(age1),id(age2),id(age3))

name,age,sex = 'kate',18,'女'
print(name,age,sex)
'''
方式4：
多个变量赋值，值的个数比变量的个数多
回收机制,变量的个数少于值的个数，并且不会报错
'''
a,*b,c = 1,2,3,4,5,6,7,8,9
print(a)
print(b)
print(c)
*a1,b1,c1 = 1,2,3,4,5,6,7,8,9
print(a1)
print(b1)
print(c1)