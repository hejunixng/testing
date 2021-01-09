# 函数
# def 函数名():

def good_job(slary, bouns, subsiby=10000, *args,**kwargs):
    # 1.subsiby = str   默认参数，缺省值
    # 有默认值的形参，只能在最后，排在必备参数后面

    # 2.位置传参
    # 不定长参数 *args （只能仿在最后）   元组： 当必备参数 和 默认参数都接受完后，不定长参数接受剩下 所有参数
    print('salary : {}'.format(slary))
    print('args {}'.format(args))
    print('kwargs {}'.format(kwargs))

    oth = 0
    for i in args:
        oth += i

    sum = slary + bouns + subsiby + oth
    print(sum, '总 {}'.format(sum))


# good_job(500, 500, 500, 1, 1, 1)        #位置传参  两种混合的话、需要先位置传参，然后关键字传参
good_job(500, bouns=500, subsiby=500,a=1,b=1,c=1)  # 关键字传参
#
# 3. 关键字传参   **kwargs   使用关键字传参的时候，  剩余参数就会存放在 **kwargs；并且以 字典保存


# 内置函数
tuple1 = (1,2,3,5)
ltuple = list(tuple1)
print(ltuple)
'''
type()
len()
str()
int()/float()
list()  转为列表
tuple()  转为元祖   元组的元素不能更改，但可以转为list更改后，再转为tuple
dict()
dict1 = dict(name='问好',age=148)

range()

'''