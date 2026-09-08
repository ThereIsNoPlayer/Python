print("请依次输入学生姓名、年龄、语文成绩、数学成绩")
name=input()
age=int(input())
c1=int(input())
c2=int(input())
sum=c1+c2
avg=sum/2
print("学生姓名:", name)
print(f"学生年龄:{age}岁")
print(f"语文成绩:{c1}分")
print(f"数学成绩:{c2}分")
print(f"总分:{sum}分")
print(f"平均分:{avg}分")
print("成绩状态:",end="")
if avg>=60:
    print("及格")
else:
    print("不及格")
