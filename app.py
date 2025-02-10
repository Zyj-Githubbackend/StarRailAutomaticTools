import tkinter as tk
from tkinter import ttk
import subprocess

# 定义按钮点击时的回调函数
def run_python_script(script_name):
    try:
        subprocess.run(['python', script_name], check=True)
        print(f"成功运行 {script_name}")
    except subprocess.CalledProcessError as e:
        print(f"运行 {script_name} 时出错: {e}")

# 创建主窗口
root = tk.Tk()
root.title("StarRail 自动化工具 by Zyj")

# 设置窗口大小及背景颜色
root.geometry("600x600")
root.configure(bg="white")

# 自定义字体
font_style = ("Arial", 12, "bold")

# 设置标题标签
label = tk.Label(root, text="StarRail 自动化工具", font=("Arial", 16, "bold"), bg="white", fg="#333")
label.pack(pady=20)


# 创建按钮并绑定事件
button1 = ttk.Button(root, text="运行原版崩铁脚本", command=lambda: run_python_script("Scripts/forOrigin.py"))
button1.pack(pady=20, ipadx=10, ipady=5)
button1.place(x=10, y=90)

button2 = ttk.Button(root, text="关闭本程序", command=lambda:exit())
button2.pack(pady=20, ipadx=10, ipady=5)
button2.place(x=200, y=300)

button3 = ttk.Button(root, text="关闭正在运行的崩铁程序", command=lambda: run_python_script("Scripts/closeStarRail.py"))
button3.pack(pady=20, ipadx=10, ipady=5)
button3.place(x=10, y=150)

# 设置按钮样式
style = ttk.Style()
style.configure("TButton",
                font=("Arial", 12, "bold"),
                background="white",  # 设置按钮背景为白色
                foreground="black",  # 设置按钮文本颜色为黑色
                padding=10)

# 修改按钮的颜色效果
style.map("TButton",
          background=[("active", "#f0f0f0")])  # 按钮悬停时背景颜色

# 启动GUI事件循环
root.mainloop()
