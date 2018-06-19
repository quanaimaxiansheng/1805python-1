d = {"name":"laowang","age":12}

keys = d.keys()#返回一个列表

for  i  in keys:
    print(i)

##效果一样
for i in d.keys():
    print(i)


values = d.values()

for i in values:
    print(i)

##效果一样
for i in d.values():

    print(i)


items  = d.items()#列表有元组[(),()]

for k,v in items:
    print("键%s值%s对"%(k,v))




