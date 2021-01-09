# # import keyword
# ctrl + / 快捷注释

# 常用数据类型 整形（int），浮点型（float）、bool、str、字典（dict）、tuple（元祖）、列表（list）
print(type(12))  # type()
print(type(11.0))

string = 'hello word!!'
print(string)
print(string[2])

# 切片 sting[索引头：索引尾：不长]  包头不包尾
print(string[0:3:2])

# l en(str) 计算字符串长度
print(string[:len(string):])


# 2. 格式化输出
# 1.%占位符 -- 占位： %s - 字符串(%s 可以写任意内容，如下面%d 可以 写成%s) ； %d - 整数 ； %f - 浮点型
name = '崽崽'
age=18

print('''
name:%s,
age:%d
''' % (name, age))

# 2. .format()   -- {}占位符   {index}里面可以指定变量顺序   更常用
name = 'notken'
age=19

print('''
name:{1},
age:{0}
''' .format(name, age))  #{indx} 可以指定format里面的变量顺序