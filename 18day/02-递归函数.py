

def cul_num(num):#递归函数最重要的是知道什么时候停
   if num == 1:
        return 1
   else:
        return num*cul_num(num-1)#5*4!


res = cul_num(5)
print(res)

