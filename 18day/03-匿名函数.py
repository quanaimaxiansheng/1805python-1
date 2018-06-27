def c_sum(a,b):
    res = a+b
    return res
res = c_sum(1,2)
print(res)

c = lambda a,b:a+b
print(c(1,2))



def cul(a,b,c):
    res = c(a,b)
    return res

c = lambda x,y:x*y
res = cul(1,2,c)
print(res)




