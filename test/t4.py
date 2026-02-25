# a=1
#
# def app(a):
#     a+=1
#     return a
# print(app(a))

def fun(a,c=2):
    return a+c
print(fun(1,2))


#参数：返回的表达式
lamb=lambda a,b:a+b
print(lamb(2,3))

#新字典=sorted(对象,规则,顺序)

dict1={'A':1,'D':5,'C':8}
dict2=sorted(dict1.items(),key=lambda item:item[1],reverse=True)
print(dict2)
#zip
for i,j in zip(range(0,4,2),range(0,5,1)):
    print(i,j)