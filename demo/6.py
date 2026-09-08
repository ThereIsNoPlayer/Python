# str=" python,java,c++ "
# st1=str.strip()
# st2=st1.split(',')
# st3=[item.upper()for item in st2]
# print(st1)
# print(st2)
# print(st3)

def plus(a,b):
    return a+b
def minus(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
a=int(input())
ob=input()
b=int(input())
if ob=="+":
    print(plus(a,b))
elif ob=="-":
    print(minus(a,b))
elif ob=="*":
    print(mul(a,b))
elif ob=="/":
    print(div(a,b))