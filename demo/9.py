import json
import os
with open('students.json', 'w+', encoding='gbk') as f:
    json.dump({}, f)
while True:
    print("1. 添加学生数据")
    print("2. 查看学生数据")
    print("3. 打印全部学生数据")
    print("0. 退出")
    choice=int(input())
    if choice==1:
        print('输入学生数据,输入"quit"退出')
        number=input('输入学号: ')
        if number == 'quit':
            break
        name=input('输入姓名: ')
        age=input('输入年龄: ')
        score=int(input('输入成绩: '))
        student = {'姓名': name, '年龄': age, '学号': number, '成绩': score}
        with open('students.json','a+',encoding='gbk') as f:
            json.dump(student, f)
    if choice == 2:
        print("输入学号: ")
        number = input()
        with open('students.json', 'r', encoding='gbk') as f:
            data = json.load(f)
            if number in data:
                print(data['姓名','年龄','学号','成绩'])
            else:
                print("未找到该学生数据")