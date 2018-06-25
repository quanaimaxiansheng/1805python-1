def sushu():
    l = []#局部变量
    for i in range(2,201):
        #i = 99
        #2-98 
        flag = False
        for j in range(2,i):
            if i%j == 0:
                flag =True
                break
        if flag == False:
            l.append(i)
    return l
res = sushu()
print(res)


