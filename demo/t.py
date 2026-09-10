import json
import os

class Student():
    def __init__(self,number,name,age,score):
        self.number=number
        self.name=name
        self.age=age
        self.score=score
    def to_dict(self):
        return {
            "学号": self.number,
            "姓名": self.name,
            "年龄": self.age,
            "成绩": self.score
        }

class StudentSystem:
    def __init__(self):
        self.file='students1.json'
        self.data={}
        self.load()
    def load(self):
        if os.path.exists(self.file):
            try:
                with open(self.file,'r') as f:
                    self.data=json.load(f)
            except:
                self.data={}
        else:
            self.data={}
    def save(self):
        with open(self.file,'w',encoding='utf-8') as f:
            json.dump(self.data,f,ensure_ascii=False,indent=4)
    def add(self):
        id=input("学号: ")
        if id in self.data:
            print("该学生已存在")
            return
        name=input("姓名: ")
        age=input("年龄: ")
        score=input("成绩: ")
        try:
            age=int(age)
            score=float(score)
            if age<0 or score<0 or score>100:
                print("范围不合规")
                return
        except ValueError:
            print("输入格式错误")
            return
        student=Student(id,name,age,score)
        self.data[id]=student.to_dict()
        self.save()
        print("Success!")

    def search(self):
        id=input("请输入要查询的学号: ")
        if id in self.data:
            stu=self.data[id]
            print(f"学号:{stu['学号']}, 姓名:{stu['姓名']}, 年龄:{stu['年龄']}, 成绩:{stu['成绩']}")
        else:
            print("此学生不存在")

    def show_all(self):
        if self.data:
            for stu in self.data.values():
                print(f"学号:{stu['学号']}, 姓名:{stu['姓名']}, 年龄:{stu['年龄']}, 成绩:{stu['成绩']}")
        else:
            print("暂无学生信息")

system=StudentSystem()
while 1:
    print('\n1. 添加学生')
    print('2. 查询学生')
    print('3. 显示所有')
    print('0. 退出')
    choice=int(input("请选择: "))
    if choice==1:
        system.add()
    elif choice==2:
        system.search()
    elif choice==3:
        system.show_all()
    elif choice==0:
        break
    else:
        print("无效选择")
