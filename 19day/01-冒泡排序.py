list = [10,100,49,2,56,3,1,37]
#list.sort()#系统提供的方法
#冒泡排序

for i in range(0,len(list)-1):
    #i 0,1,2,3,4,5,6,7
    for j in range(i+1,len(list)):
        if list[i] > list[j]:
            list[i],list[j] = list[j],list[i]
    print(list)

