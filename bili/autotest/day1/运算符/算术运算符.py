# _author:kate.wei
# date:2021/3/28
'''
python中变量的数据类型是根据赋值来决定的
算术运算符
+，-，*，/，%（取余数，取模），//（整除），**（幂运算）
除法：
python2：除法的结果只会取整数部分
python3：除法的结果会保留小数部分
整除：
整除只会取结果的整数部分
加法：
除了对数值类型进行计算之外，还可以对字符串进行连接操作
不同类型的变量，不可以相加
乘法：
除了对数值类型进行计算之外，还可以对字符串进行多次输出

'''
num1 = 10
num2 = 10
print(num1/num2)  # 结果=3.333333.....
print(num1%num2)  # 结果=1
print(num1//num2)  # 结果=3
print(num1**num2)  # 结果=1000
data = 10
str1 = 'hello'
str2 = 'python'
print(str1,str2)  #逗号的作用是输入多个值
print(str1+str2)  # 加号的作用是连接2个字符串
print(data+str1)  # 类型不同，不可以相加TypeError: unsupported operand type(s) for +: 'int' and 'str'



