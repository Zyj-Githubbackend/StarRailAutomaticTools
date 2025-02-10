import subprocess
import time
import cv2
import pyautogui
import numpy as np
from pywinauto import Application
# 可公用函数

# 运行程序
def run_the_exe(the_path_of_game):
    #  启动程序
    subprocess.Popen(the_path_of_game)

# 聚焦于程序
def focus_the_exe(the_path_of_game,key):
    while True:
        try:
            # 连接到正在运行的应用程序（假设程序已经运行）
            app = Application(backend="uia").connect(path=the_path_of_game)

            # 获取程序的主窗口
            window = app.window(title_re=f".*{key}.*")  # 使用正则匹配窗口标题

            # 将窗口置于最前面
            window.set_focus()  # 聚焦窗口

            print("窗口已获取、聚焦并居中")
            break  # 成功找到并聚焦窗口后跳出循环

        except Exception as e:
            # 如果程序没有找到窗口，等待一段时间然后继续查找
            print(f"未找到窗口，继续查找... 错误: {e}")
            time.sleep(1)  # 每次等待 1 秒钟后继续查找

# 不断根据图片识别点击图片中心
def find_and_click_image(template_path):
    #  给时间待游戏加载 提供容错
    time.sleep(1)
    while True:
        # 截图：截取当前屏幕
        screenshot = pyautogui.screenshot()  # 获取当前屏幕截图
        screenshot = np.array(screenshot)  # 转换为 numpy 数组
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)  # 转换颜色格式

        # 读取模板图像
        template = cv2.imread(template_path)
        w, h = template.shape[:2]  # 获取模板图像的宽度和高度

        # 使用模板匹配来寻找图像的位置
        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

        # 找到匹配位置，阈值可以根据需要调整
        threshold = 0.9  # 设置匹配的阈值
        loc = np.where(result >= threshold)

        if len(loc[0]) > 0:
            # 找到第一个匹配的位置（图像左上角）
            x, y = loc[1][0], loc[0][0]

            # 计算图像的中心位置
            center_x = x + h // 2
            center_y = y + w // 2

            # 使用 pyautogui 点击该位置
            pyautogui.click(center_x, center_y)

            print(f"图像匹配成功，点击位置：({center_x}, {center_y})")
            break  # 成功找到并点击后跳出循环
        else:
            time.sleep(1)  # 如果没有找到匹配，等待1秒后继续检测

# 根据图片识别点击图片靠右的四等分点中心
def find_and_click_right_of_image(template_path):
    # 点图片y轴中心 x轴等分点靠右点

    #  给时间待游戏加载 提供容错
    time.sleep(1)

    while True:
        # 截图：截取当前屏幕
        screenshot = pyautogui.screenshot()  # 获取当前屏幕截图
        screenshot = np.array(screenshot)  # 转换为 numpy 数组
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)  # 转换颜色格式

        # 读取模板图像
        template = cv2.imread(template_path)
        w, h = template.shape[:2]  # 获取模板图像的宽度和高度
        # 使用模板匹配来寻找图像的位置
        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

        # 找到匹配位置，阈值可以根据需要调整
        threshold = 0.9  # 设置匹配的阈值
        loc = np.where(result >= threshold)

        if len(loc[0]) > 0:
            # 找到第一个匹配的位置（图像左上角）
            x, y = loc[1][0], loc[0][0]

            # 计算点击图像的位置
            click_x = x + int((h/4)*3)
            click_y = y + w//2

            # 使用 pyautogui 点击该位置
            pyautogui.click(click_x, click_y)
            print(f"图像匹配成功，点击位置：({click_x}, {click_y})")
            break  # 成功找到并点击后跳出循环
        else:
            time.sleep(1)  # 如果没有找到匹配，等待1秒后继续检测

# 根据图片识别按下某个键位
def find_image_press_key(template_path,key:str):
    #  给时间待游戏加载 提供容错
    time.sleep(1)

    while True:
        # 截图：截取当前屏幕
        screenshot = pyautogui.screenshot()  # 获取当前屏幕截图
        screenshot = np.array(screenshot)  # 转换为 numpy 数组
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)  # 转换颜色格式

        # 读取模板图像
        template = cv2.imread(template_path)
        w, h = template.shape[:2]  # 获取模板图像的宽度和高度

        # 使用模板匹配来寻找图像的位置
        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

        # 找到匹配位置，阈值可以根据需要调整
        threshold = 0.97  # 设置匹配的阈值
        loc = np.where(result >= threshold)

        if len(loc[0]) > 0:
            # 找到第一个匹配的位置（图像左上角）
            x, y = loc[1][0], loc[0][0]

            # 计算图像的中心位置
            center_x = x + w // 2
            center_y = y + h // 2

            # 使用 pyautogui   按下某个键位
            pyautogui.press(key)
            print(f"图像匹配成功，按下键位：({key})")
            break  # 成功找到并点击后跳出循环
        else:
            time.sleep(1)  # 如果没有找到匹配，等待1秒后继续检测

# 根据图片识别点击图片中心  一次性  返回布尔值
def find_and_click_image_once(template_path)->bool:
    #  给时间待游戏加载 提供容错
    time.sleep(1)

    # 截图：截取当前屏幕
    screenshot = pyautogui.screenshot()  # 获取当前屏幕截图
    screenshot = np.array(screenshot)  # 转换为 numpy 数组
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)  # 转换颜色格式

    # 读取模板图像
    template = cv2.imread(template_path)
    w, h = template.shape[:2]  # 获取模板图像的宽度和高度

    # 使用模板匹配来寻找图像的位置
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

    # 找到匹配位置，阈值可以根据需要调整
    threshold = 0.9  # 设置匹配的阈值
    loc = np.where(result >= threshold)

    if len(loc[0]) > 0:
        # 找到第一个匹配的位置（图像左上角）
        x, y = loc[1][0], loc[0][0]

        # 计算图像的中心位置
        center_x = x + h // 2
        center_y = y + w // 2

        # 使用 pyautogui 点击该位置
        pyautogui.click(center_x, center_y)

        print(f"图像匹配成功，点击位置：({center_x}, {center_y})")
        return True
    return False

# 关闭某个程序
def kill_process_by_name(process_name):
    try:
        # 检查进程是否存在
        result = subprocess.run(f'tasklist /FI "IMAGENAME eq {process_name}"', capture_output=True, text=True, shell=True)
        if process_name in result.stdout:
            # 如果进程存在，使用 taskkill 命令强制结束进程
            subprocess.run(f'taskkill /IM {process_name} /F', check=True, shell=True)
            print(f"进程 {process_name} 已被强制关闭")
        else:
            print(f"进程 {process_name} 不存在，无需关闭")
    except subprocess.CalledProcessError as e:
        print(f"无法关闭进程 {process_name}，错误信息：{e}")

# 定义按钮点击时的回调函数
def run_python_script(script_name):
    try:
        subprocess.run(['python', script_name], check=True)
        print(f"成功运行 {script_name}")
    except subprocess.CalledProcessError as e:
        print(f"运行 {script_name} 时出错: {e}")