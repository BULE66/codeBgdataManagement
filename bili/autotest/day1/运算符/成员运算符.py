# _author:kate.wei
# date:2021/3/28

'''
成员运算符，用来判断指定的内容是否存在变量中，例如：in，not in
成员运算符返还的结果是布尔值，True或者False

注意类型是不可分割的整体，因此不可以对数值类型用in， not in
'''
str1 = 'hello python'
print('hll' in str1)
data = 10
print(1 in data)  # TypeError: argument of type 'int' is not iterable
