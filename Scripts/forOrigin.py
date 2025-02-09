# 用于原版启动
#基于 1920*1080 窗口

import subprocess
import time
import cv2
import pyautogui
import numpy as np

from pywinauto import Application


#模板图像路径
clickToLogin_path = "../components/login/clickToLogin.png"
phone_path = "../components/inGame/phone.png"
enTrust_path = "../components/inGame/enTrust.png"
getTheEnTrust_path = "../components/inGame/getTheEnTrust.png"
getTheEnTrustAgain_path = "../components/inGame/enTrustAgain.png"
zhinan_path = "../components/inGame/zhinan.png"
tili1_path = "../components/inGame/Tili1.png"
yiqi_path = "../components/inGame/yiqi.png"
yiqi1_path = "../components/inGame/yiqi1.png"
exit_path = "../components/inGame/exit.png"
challenge_path = "../components/inGame/challenge.png"
zhiyuan_path = "../components/inGame/zhiyuan.png"
huangquan_path = "../components/inGame/huangquan.png"
enqueue_path = "../components/inGame/enqueue.png"
startChallenge_path = "../components/inGame/startChanllenge.png"
oneMoreTime_path = "../components/inGame/oneMoreTime.png"


# 游戏路径
path = "E:\miHoYo Launcher\games\Star Rail Game\StarRail.exe"


def run_the_exe(the_path_of_game):
    #  启动程序
    subprocess.Popen(the_path_of_game)

def focus_the_exe(the_path_of_game):
    while True:
        try:
            # 连接到正在运行的应用程序（假设程序已经运行）
            app = Application(backend="uia").connect(path=the_path_of_game)

            # 获取程序的主窗口
            window = app.window(title_re=".*崩坏.*")  # 使用正则匹配窗口标题

            # 将窗口置于最前面
            window.set_focus()  # 聚焦窗口

            print("窗口已获取、聚焦并居中")
            break  # 成功找到并聚焦窗口后跳出循环

        except Exception as e:
            # 如果程序没有找到窗口，等待一段时间然后继续查找
            print(f"未找到窗口，继续查找... 错误: {e}")
            time.sleep(1)  # 每次等待 1 秒钟后继续查找

def find_and_click_image(template_path):
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


def find_and_click_right_of_image(template_path):
    # 点图片y轴中心 x轴等分点靠右点
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


def find_image_press_key(template_path,key:str):
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

# 主函数
DEBUG = True

if DEBUG:
    print("----开始运行------")
    # 运行
    run_the_exe(path)

    focus_the_exe(path)
    # 登录
    find_and_click_image(clickToLogin_path)
    # 进入手机
    find_image_press_key(phone_path,'esc')

    # 委托
    find_and_click_image(enTrust_path)

    find_and_click_image(getTheEnTrust_path)

    find_and_click_image(getTheEnTrustAgain_path)

    find_and_click_image(exit_path)
     # 点击指南
    find_and_click_image(zhinan_path)

    # 清体力
    find_and_click_image(tili1_path)

    # 刷遗器准备

    find_and_click_image(yiqi_path)

    find_and_click_right_of_image(yiqi1_path)

    #刷遗器
    find_and_click_image(challenge_path)

    find_and_click_image(zhiyuan_path)

    find_and_click_image(huangquan_path)

    find_and_click_image(enqueue_path)

    find_and_click_image(startChallenge_path)

    while True:
        find_and_click_image(oneMoreTime_path)
else:
    # 刷遗器   直接进入具体挑战的页面后进行此处即可
    find_and_click_image(challenge_path)

    find_and_click_image(zhiyuan_path)

    find_and_click_image(huangquan_path)

    find_and_click_image(enqueue_path)

    find_and_click_image(startChallenge_path)

    while True:
        find_and_click_image(oneMoreTime_path)