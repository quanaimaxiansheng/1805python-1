'''
身份证

姓名：老王
出生年月：23
地址：隔壁
民族：爱新觉罗
性别：男

key:value

键值对

'''
#列表  []
#元组  ()
#字典  {}
id_card =  {"name":"老王","birthday":"1991.12.12","address":"隔壁","eth":"爱新觉罗","sex":"男"}

print(id_card)
print(type(id_card))

#新增
id_card["birthday"] = 180#如果key存在，则修改值，如果不存在，新增
print(id_card)


id_card.setdefault("birthday",180)#如果key存在，则不修改值，如果key不存在，则添加
id_card.setdefault("aaa",11)
print(id_card)

#查找
print(id_card["name"])#如果key不存在 报错
print(id_card.get("name"))#如果key不存在 返回None

#修改
id_card["name"] = "老宋"
print(id_card) 

#删除
#id_card.pop("name")
#print(id_card)


id_card.popitem()
print(id_card)

id_card.popitem()#随机删除，字典是无序的

del id_card["name"]#系统提供的删除方法
#清空
#id_card.clear()


#合并
d = {"11":"aa","22":"bb","eth":"满族"}
id_card.update(d)#如果key存在，则会覆盖掉
print(id_card)



