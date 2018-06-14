'''
只能被1和本身的数整除

任何数能被1和本身整除

任何数都不能被比它大的数整除

example：

149
要从2-148能整除149 如果其中有1个数整除了149 这个149一定不是素数

'''
list = [] 
for  i in range(100,201):
    '''
    你跟你朋友打赌，堵100和200的都是素数
    每验证一个数你要1块钱
    '''
    money = 1#每次都放1块钱 来当做押金
    for j in range(2,i):#你朋友去验证
        # i = 150
        if i%j == 0:
            money = 0 #验证失败，押金归零
            break
    
    if money == 1:#判断一下钱在不在 如果在的话就是素数
        list.append(i)

print(list)
#求和
msum = 0
for i in list:
    msum +=i #msum = msum+i

print("和是%d"%msum)
#print("和是%d"%sum(list))

#倒序
list.reverse()
print(list)
        
