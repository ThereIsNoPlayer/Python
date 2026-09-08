# 1.	创建一个学生信息字典，包含姓名、学号、成绩，序列化为JSON字符串并打印。
# 2.	将学生信息写入student.json文件，格式化缩进输出。
# 3.	读取student.json文件，解析为Python字典，打印学生姓名。
# 4.	创建包含3名学生的列表，批量写入JSON文件，再读取并遍历输出所有学生姓名。

import json
stu_dict={"name":"Alice","id":"001","score":85}
with open('data.json', 'w+', encoding='utf-8') as f:
    json.dump(stu_dict,f,ensure_ascii=False,indent=4)

with open('data.json', 'r') as f:
    data=json.load(f)
print(data)

with open('data.json', 'r') as f:
    data=json.load(f)
print(data['name'])

s_l=[
    {"name":"bob","id":"002","score":90},
    {"name":"charlie","id":"003","score":75},
    {"name":"dick","id":"004","score":80},
]

with open('data1.json', 'w+', encoding='utf-8') as f:
    json.dump(s_l,f,ensure_ascii=False,indent=4)
with open('data1.json', 'r') as f:
    data=json.load(f)
for name in data:
    print(name["name"])