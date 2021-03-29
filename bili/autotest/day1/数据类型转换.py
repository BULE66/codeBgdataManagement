# _author:kate.wei
# date:2021/3/28
'''
数据类型转换
作用：将其他数据类型转为指定的数据类型
数值类型：int ,float, bool、字符串类型
原则：变量上包裹你要转的数据类型的方法就可以了
str()
int()
float()

'''
# int --->str
data = 10
res = str(data)
print(res,type(res))
data = 'hello'
res1 = bool(data) # True:非0值或者非空值转为bool,都是true，0和空值转为bool,都是false
print(res1,type(res1))
# str-->int/float 必须满足一个前提，字符的内容只包含数字的时候才可以
str1 = '123'
res2 = int(str1)
print(res2,type(res2))
