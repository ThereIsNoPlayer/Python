# 作业：学生成绩管理系统
# 1.	完成斗地主洗牌发牌程序
#
# import random
# colors=["♠","♥","♦","♣"]
# nums=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
# poker=[]
# for c in colors:
#     for n in nums:
#         poker.append([c,n])
# poker.append("大王")
# poker.append("小王")
# random.shuffle(poker)
# # print(poker)
# p1=[]
# p2=[]
# p3=[]
# p4=[]
# for i in range(17):
#     p1.append(poker.pop())
#     p2.append(poker.pop())
#     p3.append(poker.pop())
#
# p4=poker
# print(p1)
# print(p2)
# print(p3)
# print(p4)

# 2.	程序提供菜单功能：
# Plaintext
# ===学生成绩管理系统===
# 1. 添加学生
# 2. 删除学生
# 3. 修改成绩
# 4. 查询学生成绩
# 5. 显示所有学生
# 6. 退出
# 2.	学生信息包含：学号、姓名、语文成绩、数学成绩；
# 3.	使用字典存储学生信息，学号作为键，值为学生信息字典；
# 4.	实现全部菜单功能，输入对应编号执行操作；
# 5.	额外功能：计算并显示所有学生的平均分、最高分、最低分。

dict_stu={}

while 1:
    print(f"""
    1. 添加学生
    2. 删除学生
    3. 修改成绩
    4. 查询学生成绩
    5. 显示所有学生
    6. 退出
    7. 显示所有学生的平均分、最高分、最低分
    """)
    choice=input("请输入菜单编号")
    if choice=="1":
            print("添加学生")
            stu_id=input("学号")
            if stu_id in dict_stu:
                print("已存在")
            else:
                name=input("姓名")
                chinese=int(input("语文成绩"))
                math=int(input("数学成绩"))
                dict_stu[stu_id]={"姓名":name,"语文":chinese,"数学":math}
                print("success!")
    if choice=="2":
            print("删除学生")
            stu_id=input("学号")
            if stu_id in dict_stu:
                del dict_stu[stu_id]
                print("success!")
            else:
                print("学生不存在")
    if choice=="3":
            print("修改成绩")
            stu_id=input("学号")
            if stu_id in dict_stu:
                name=input("姓名")
                chinese=int(input("语文成绩"))
                math=int(input("数学成绩"))
                dict_stu[stu_id]={"姓名":name,"语文":chinese,"数学":math}
                print("success!")
            else:
                print("学生不存在")
    if choice=="4":
            print("查询学生成绩")
            stu_id=input("学号")
            if stu_id in dict_stu:
                print(dict_stu[stu_id])
            else:
                print("学生不存在")
    if choice=="5":
        print("显示所有学生")
        if dict_stu:
            for id, info in dict_stu.items():
                print(f"学号: {id}, 姓名: {info['姓名']}, 语文: {info['语文']}, 数学: {info['数学']}")
        else:
            print("列表中没有学生")


    if choice=="6":
        print("退出")
        break

    if choice=="7":
        sum_chinese=sum(info['语文'] for info in dict_stu.values())
        sum_math=sum(info['数学'] for info in dict_stu.values())
        avg_chinese=sum_chinese/len(dict_stu) if dict_stu else 0
        avg_math=sum_math/len(dict_stu) if dict_stu else 0
        max_chinese=max(info['语文'] for info in dict_stu.values()) if dict_stu else 0
        min_chinese=min(info['语文'] for info in dict_stu.values()) if dict_stu else 0
        max_math=max(info['数学'] for info in dict_stu.values()) if dict_stu else 0
        min_math=min(info['数学'] for info in dict_stu.values()) if dict_stu else 0
        print(f"平均分 - 语文: {avg_chinese:.2f}, 数学: {avg_math:.2f}")
        print(f"最高分 - 语文: {max_chinese}, 数学: {max_math}")
        print(f"最低分 - 语文: {min_chinese}, 数学: {min_math}")