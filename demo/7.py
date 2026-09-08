# 1.	编写程序，向student.txt写入3名学生的姓名和成绩，每行一条学生信息。
# 2.	编写程序，读取student.txt的全部内容，控制台打印输出。
# 3.	逐行读取student.txt，统计学生总人数。
# 4.	编写程序，读取一个文本文件，统计文件中的字符总数与总行数。

with open('../student.txt', 'w+') as f:
    f.write('Alice,85\n')
    f.write('Bob,90\n')
    f.write('Charlie,78\n')

with open('../student.txt', 'r') as f1:
    read=f1.read()
    print(read)

with open('../student.txt', 'r') as f2:
    r=f2.readlines()
    total=0
    for lines in r:
        total+=1
    print('total:',total)

with open('../student.txt', 'r') as f3:
    count=f3.read()
    print('Character count:', len(count))
    print('Line count:', count.count('\n'))