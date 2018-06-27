list = [1,3,4,7,10,45,60,80,100]

#第一种
i = 0
while i < len(list):
    if list[i] == 80:
        print("索引是%d"%i)
        break
    i+=1
#第二种
position = list.index(80)
print("索引是%d"%position)
#第三种
for p,i in enumerate(list):
    if i == 80:
        print("索引是%d"%p)
        break
#第四种 二分法 列表一定是有序的
list = [1,3,4,7,10,45,60,80,100] 
min = 0#最小索引
max = len(list) - 1#最大索引
count = 80
while True:
    print("找了")
    center = int((min+max)/2)#中间
    if list[center] > count:
        max = center- 1
    elif list[center] < count:
        min = center + 1
    elif list[center] == count:
        print("索引是%d"%center)
        break




