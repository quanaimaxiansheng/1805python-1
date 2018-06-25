def c_sum(a,b,d,c=100,f=200):#缺省参数一定要放到最后面
    print(a)
    print(b)
    print(c)
    print(d)


#c_sum(1,2,3,4)


def d_sum(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    sum = 0
    sum = a + b
    for i in args:
        sum+=i
    '''
    for v in kwargs.values():
        sum+=v
    '''
    
    ''' 
    for k in kwargs:
        sum+=kwargs[k]
    '''

    '''
    for k in kwargs.keys():
         sum+=kwargs[k]
    '''
    for k,v in kwargs.items():
        sum+=v

    return sum


#d_sum(1,2,3,4,5,6,7,8,9,10,age=7,wei= 12)
t = (1,2,3,4,5,6)
d = {"age":12,"weight":24}
res = d_sum(1,2,*t,**d)#拆包
print(res)
'''
把我传进去的所有的数字和算出来，并返回，并打印
'''

