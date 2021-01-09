print(str(10) + 'def')    # int(),str(),float()

print('love you ' * 10)

print(10 % 3)  # 取余

# 2.赋值 = += -=

# 3. 比较运算符 ： > >= <= < ==  !=   看短路

# 4.逻辑运算符 and、or、not（非）

# 5.成员运算符  in 、not in
print('h' in 'hello')


'''
1.列表 []  list
2.列表元素可以包含任意数据类型：整形、浮点数、bool、列表
3.有顺序，索引值
4.列表元素  增删改
5.元素可重复
'''
list1 = [1, 2, 3, True,'dasd']
print(list1[:len(list1):2])

list1.append('在列表最后')   #append(str)
list1.insert(2, '指定位置')  #insert(index,str)
list1.pop(1)     # 默认删除最后一个
list1.remove(3)    #remove(str) 删除列表里面的 指定元素，如果有重复，会删除先发现的元素

# 修改
list1[0] = '已更改'

print(list1)


'''
元祖 tuple()
1.元素可为 任意类型 （元素类型
3.元素可以重复
2.元素不可以更改！！
'''
tuple1 = ('大','小','tuple')
#  tuple1[0] = 'as'
print(tuple1)

'''
字典 dict  {key:value}
1.描述对象基本信息
2.key:除了列表list 和 字典 dict之外都可以（不可迭代），value都可以
取值：dict[key] 、 dict1.get(key)
3. 没有顺序
4.key不能改变，value可以改变
'''
dict1 = {'name':'holly','age':18,'hobby':'python好难'}

# dict 取值
print(dict1['name'])
print(dict1.get('name'))

print(dict1.keys())   #获取所有key
print(dict1.values())
print(dict1.items())  # 获取dict的 key、value

dict1['hobby']= 'gogogo'

dict1.pop('hobby')    # dict没有顺序，pop要加元素
print(dict1)
#元祖、列表、字典的区别？

listt = {(1,2) : 'GG'}
print(listt)


# 控制流
#  if elif else
# 如果是 if []  这种空值，就是false  非空就是真 if 1 、 2之类

money = 200
if money >200:
    print('fuck them all')
elif money >= 100:
    print('fuck them')
else :
    print('dayday fuck')

# for循环
print('*' * 20)
str1 = 'lemon'

for item in str1:
    print(item)

# range(start,stop.step)  生成一个整数列表list   for循环一起用
for i in range(1,30,5):
    print(i)