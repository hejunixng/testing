
dit1 = {"class":45,
        "num":20}

if dit1['num'] > 5:
    print(dit1['num'])


str1 = 'string'
sttlist = list(str1)
print(sttlist)

list2 = [1,2,3,4]
num = 0
for i in list2:
    num += i
print(type(num))

def my_type (obj):
    print(type(obj) == "<class 'list'>")
    # if type(obj) in 'list':
    #     print(len(obj))


my_type([1,2,3])