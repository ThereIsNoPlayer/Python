import math
import random
import tkinter as tk

# ==================== 用户自定义名册数据 ====================
DUNGEONS = [
    "破碎王座",
    "异端深渊",
    "预言",
    "贪婪之握",
    "二象性",
    "守望者尖塔",
    "深渊机灵",
    "战争领主的废墟",
    "晚星之主",
    "分离教义",
    "平衡",
]

RAIDS = [
    "最后一愿",
    "深岩墓室",
    "救赎花园",
    "玻璃拱顶",
    "门徒誓约",
    "国王的陨落",
    "克洛塔的末日",
    "梦魇根源",
    "救赎的边缘",
    "永恒沙漠",
    "永恒沙漠(史诗)",
]

# 转盘调色盘 (11种色值自动循环)
COLORS = [
    "#1E293B",
    "#334155",
    "#1E3A8A",
    "#1D4ED8",
    "#065F46",
    "#047857",
    "#581C87",
    "#7E22CE",
    "#831843",
    "#9F1239",
    "#431407",
]


class Destiny2CustomSpinner:

    def __init__(self, root):
        self.root = root
        self.root.title("命运2 随机转盘")
        self.root.geometry("540x650")
        self.root.configure(bg="#0F172A")
        self.root.resizable(False, False)

        self.current_angle = 0
        self.is_spinning = False
        self.mode = "DUNGEON"  # 默认地牢模式
        self.current_list = DUNGEONS

        # 1. 标题
        title = tk.Label(
            root,
            text="❖ 随机转盘 ❖",
            font=("Consolas", 15, "bold"),
            fg="#38BDF8",
            bg="#0F172A",
            pady=10,
        )
        title.pack()

        # 2. 模式切换按钮
        mode_frame = tk.Frame(root, bg="#0F172A")
        mode_frame.pack(pady=2)

        self.btn_dungeon = tk.Button(
            mode_frame,
            text=" 地牢 ",
            font=("Microsoft YaHei", 10, "bold"),
            bg="#0284C7",
            fg="#FFFFFF",
            relief="flat",
            padx=15,
            pady=4,
            command=lambda: self.switch_mode("DUNGEON"),
        )
        self.btn_dungeon.pack(side="left", padx=5)

        self.btn_raid = tk.Button(
            mode_frame,
            text=" 突袭 ",
            font=("Microsoft YaHei", 10),
            bg="#334155",
            fg="#94A3B8",
            relief="flat",
            padx=15,
            pady=4,
            command=lambda: self.switch_mode("RAID"),
        )
        self.btn_raid.pack(side="left", padx=5)

        # 3. 画布
        self.canvas = tk.Canvas(
            root, width=440, height=440, bg="#0F172A", highlightthickness=0
        )
        self.canvas.pack(pady=10)

        # 4. 抽取按钮
        self.spin_button = tk.Button(
            root,
            text=" 开始抽取 ",
            font=("Microsoft YaHei", 12, "bold"),
            bg="#EAB308",
            fg="#0F172A",
            activebackground="#CA8A04",
            activeforeground="#FFFFFF",
            relief="flat",
            padx=25,
            pady=8,
            command=self.start_spin,
        )
        self.spin_button.pack(pady=5)

        # 5. 结果显示
        self.result_label = tk.Label(
            root,
            text="点击按钮挑选今天打什么",
            font=("Microsoft YaHei", 11),
            fg="#94A3B8",
            bg="#0F172A",
        )
        self.result_label.pack(pady=5)

        self.draw_wheel()

    def switch_mode(self, new_mode):
        if self.is_spinning or self.mode == new_mode:
            return

        self.mode = new_mode
        if self.mode == "DUNGEON":
            self.current_list = DUNGEONS
            self.btn_dungeon.config(
                bg="#0284C7", fg="#FFFFFF", font=("Microsoft YaHei", 10, "bold")
            )
            self.btn_raid.config(
                bg="#334155", fg="#94A3B8", font=("Microsoft YaHei", 10)
            )
            self.result_label.config(
                text="已切换至：地牢模式", fg="#94A3B8"
            )
        else:
            self.current_list = RAIDS
            self.btn_raid.config(
                bg="#0284C7", fg="#FFFFFF", font=("Microsoft YaHei", 10, "bold")
            )
            self.btn_dungeon.config(
                bg="#334155", fg="#94A3B8", font=("Microsoft YaHei", 10)
            )
            self.result_label.config(
                text="已切换至：突袭模式", fg="#94A3B8"
            )

        self.draw_wheel()

    def draw_wheel(self):
        self.canvas.delete("all")
        num_items = len(self.current_list)
        slice_angle = 360 / num_items
        cx, cy, radius = 220, 220, 200

        for i, item in enumerate(self.current_list):
            start_deg = self.current_angle + i * slice_angle
            color = COLORS[i % len(COLORS)]

            # 扇区
            self.canvas.create_arc(
                cx - radius,
                cy - radius,
                cx + radius,
                cy + radius,
                start=start_deg,
                extent=slice_angle,
                fill=color,
                outline="#0F172A",
                width=2,
            )

            # 文字
            mid_angle = math.radians(start_deg + slice_angle / 2)
            tx = cx + (radius * 0.65) * math.cos(mid_angle)
            ty = cy - (radius * 0.65) * math.sin(mid_angle)

            self.canvas.create_text(
                tx,
                ty,
                text=item,
                fill="#F8FAFC",
                font=("Microsoft YaHei", 8, "bold"),
            )

        # 指针 (顶部 12 点钟)
        self.canvas.create_polygon(
            210, 10, 230, 10, 220, 38, fill="#EF4444", outline="#FFFFFF", width=2
        )
        # 中心装饰
        self.canvas.create_oval(
            cx - 16, cy - 16, cx + 16, cy + 16, fill="#0F172A", outline="#38BDF8"
        )

    def start_spin(self):
        if self.is_spinning:
            return

        self.is_spinning = True
        self.spin_button.config(state="disabled")
        self.result_label.config(text="大粪精选中...", fg="#FBBF24")

        total_rotation = 360 * random.randint(6, 9) + random.uniform(0, 360)
        steps = 85
        self.animate_spin(total_rotation, steps, 0)

    def animate_spin(self, remaining_angle, total_steps, current_step):
        if current_step >= total_steps:
            self.is_spinning = False
            self.spin_button.config(state="normal")
            self.calculate_winner()
            return

        t = current_step / total_steps
        step_angle = (1 - (1 - t) ** 3) * remaining_angle - (
            1 - (1 - (current_step - 1) / total_steps) ** 3
        ) * remaining_angle if current_step > 0 else 0

        self.current_angle = (self.current_angle + step_angle) % 360
        self.draw_wheel()

        delay = int(18 + (t**2) * 55)
        self.root.after(
            delay,
            lambda: self.animate_spin(
                remaining_angle, total_steps, current_step + 1
            ),
        )

    def calculate_winner(self):
        num_items = len(self.current_list)
        slice_angle = 360 / num_items

        normalized_angle = (90 - self.current_angle) % 360
        winning_index = int(normalized_angle // slice_angle) % num_items

        winner = self.current_list[winning_index]
        mode_name = "地牢" if self.mode == "DUNGEON" else "突袭"
        self.result_label.config(
            text=f"🎯 今日{mode_name}目标：【{winner}】", fg="#34D399"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = Destiny2CustomSpinner(root)
    root.mainloop()