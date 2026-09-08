# for i in range(1,11):
#     print(i)


# j=1
# sum=0
# while j<=10:
#     sum=j+sum
#     j+=1
# print(sum)

#
# for i in range(1,10):
#     print("\n")
#     for j in range(1,i+1):
#         print(f"{i}*{j}={i*j}", end=" ")


print("请输入学生姓名和对应分数")
namel=[]
scl=[]
for i in range(3):
    name=input()
    sc=float(input())
    namel.append(name)
    scl.append(sc)
total=sum(scl)
avg=total/3
maxs=max(scl)
mins=min(scl)
for j in range(3):
    n=namel[j]
    sc=scl[j]
    if sc>=90:
        g="优秀"
    elif sc>=80:
        g="良好"
    elif sc>=60:
        g="及格"
    else:
        g="不及格"
    print("姓名:",n,"分数:",sc,"等级:",g)

print("平均分:",avg)
print("最高分:",maxs)
print("最低分:",mins)
