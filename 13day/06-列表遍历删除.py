list = [1,2,3,4,5,6,7,8,9]

#有坑
'''
for position,i in enumerate(list):
    list.pop(position)
'''

for i in range(len(list)-1,-1,-1):
    list.pop(i)
    

print(list)
