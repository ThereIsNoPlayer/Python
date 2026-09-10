import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

np.random.seed(42)
scores = np.random.randint(0, 101, size=(5, 4))
print("=" * 50)
print("学生成绩表（5名学生 × 4门课程）")
print("=" * 50)
print(scores)
print()

print("=" * 50)
print("数组属性")
print("=" * 50)
print(f"形状 (shape): {scores.shape}")
print(f"维度 (ndim): {scores.ndim}")
print(f"元素总数 (size): {scores.size}")
print(f"数据类型 (dtype): {scores.dtype}")
print()

print("=" * 50)
print("数据统计")
print("=" * 50)
total_sum = np.sum(scores)
total_mean = np.mean(scores)
print(f"所有成绩的总分: {total_sum}")
print(f"所有成绩的平均分: {total_mean:.2f}")

course_mean = np.mean(scores, axis=0)
print(f"每门课的平均分: {course_mean}")

student_mean = np.mean(scores, axis=1)
print(f"每个学生的平均分: {student_mean}")

max_score = np.max(scores)
min_score = np.min(scores)
max_idx = np.unravel_index(np.argmax(scores), scores.shape)
min_idx = np.unravel_index(np.argmin(scores), scores.shape)
print(f"全班最高分: {max_score}，位置: 第{max_idx[0]+1}名学生，第{max_idx[1]+1}门课")
print(f"全班最低分: {min_score}，位置: 第{min_idx[0]+1}名学生，第{min_idx[1]+1}门课")
print()

print("=" * 50)
print("数据处理（所有成绩+5，超过100按100计）")
print("=" * 50)
scores_plus = scores + 5
scores_plus = np.where(scores_plus > 100, 100, scores_plus)
print("加分后的成绩表：")
print(scores_plus)
print()

student_total = np.sum(scores, axis=1)

plt.figure(figsize=(10, 4))
plt.bar(range(1, 6), student_total, color='skyblue', edgecolor='black')
plt.title('5名学生的总分')
plt.xlabel('学生编号')
plt.ylabel('总分')
plt.xticks(range(1, 6))
for i, v in enumerate(student_total):
    plt.text(i+1, v+2, str(v), ha='center', va='bottom')
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 4))
plt.plot(range(1, 5), course_mean, marker='o', linestyle='-', color='red', linewidth=2)
plt.title('4门课程的平均分')
plt.xlabel('课程编号')
plt.ylabel('平均分')
plt.xticks(range(1, 5))
plt.ylim(0, 100)
for i, v in enumerate(course_mean):
    plt.text(i+1, v+1, f'{v:.1f}', ha='center', va='bottom')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()

with open('成绩统计结果.txt', 'w', encoding='utf-8') as f:
    f.write("=" * 50 + "\n")
    f.write("学生成绩统计结果\n")
    f.write("=" * 50 + "\n\n")
    f.write("原始成绩表（5名学生 × 4门课程）：\n")
    f.write(str(scores) + "\n\n")
    f.write("数组属性：\n")
    f.write(f"形状: {scores.shape}\n")
    f.write(f"维度: {scores.ndim}\n")
    f.write(f"元素总数: {scores.size}\n")
    f.write(f"数据类型: {scores.dtype}\n\n")
    f.write("数据统计：\n")
    f.write(f"所有成绩的总分: {total_sum}\n")
    f.write(f"所有成绩的平均分: {total_mean:.2f}\n")
    f.write(f"每门课的平均分: {course_mean}\n")
    f.write(f"每个学生的平均分: {student_mean}\n")
    f.write(f"全班最高分: {max_score}，位置: 第{max_idx[0]+1}名学生，第{max_idx[1]+1}门课\n")
    f.write(f"全班最低分: {min_score}，位置: 第{min_idx[0]+1}名学生，第{min_idx[1]+1}门课\n\n")
    f.write("加分后成绩表（所有成绩+5，超过100按100计）：\n")
    f.write(str(scores_plus) + "\n\n")
    f.write("可视化数据：\n")
    f.write(f"5名学生的总分: {student_total}\n")
    f.write(f"4门课程的平均分: {course_mean}\n")

print("\n统计结果已保存到文件：成绩统计结果.txt")