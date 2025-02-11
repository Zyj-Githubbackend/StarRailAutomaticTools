# 用于原版启动
#基于 1920*1080 窗口
import time

from utils.sharedFunc import run_the_exe, focus_the_exe, find_image_press_key, find_and_click_image, find_and_click_right_of_image,find_and_click_image_once
from config import THE_PATH_OF_ORIGIN_GAME,THE_PATH_OF_THIS_SCRIPT

#模板图像绝对路径
clickToLogin_path = f"{THE_PATH_OF_THIS_SCRIPT}/StarRail/components/login/clickToLogin.png"
phone_path = f"{THE_PATH_OF_THIS_SCRIPT}/StarRail/components/inGame/phone.png"
enTrust_path = f"{THE_PATH_OF_THIS_SCRIPT}/StarRail/components/inGame/enTrust.png"
getTheEnTrust_path = f"{THE_PATH_OF_THIS_SCRIPT}/StarRail/components/inGame/getTheEnTrust.png"
getTheEnTrustAgain_path = f"{THE_PATH_OF_THIS_SCRIPT}/StarRail/components/inGame/enTrustAgain.png"
zhinan_path = f"{THE_PATH_OF_THIS_SCRIPT}/StarRail/components/inGame/zhinan.png"
tili1_path = f"{THE_PATH_OF_THIS_SCRIPT}/StarRail/components/inGame/Tili1.png"
yiqi_path = f"{THE_PATH_OF_THIS_SCRIPT}/StarRail/components/inGame/yiqi.png"
yiqi1_path = f"{THE_PATH_OF_THIS_SCRIPT}/StarRail/components/inGame/yiqi1.png"
exit_path = f"{THE_PATH_OF_THIS_SCRIPT}/StarRail/components/inGame/exit.png"
challenge_path = f"{THE_PATH_OF_THIS_SCRIPT}/StarRail/components/inGame/challenge.png"
zhiyuan_path = f"{THE_PATH_OF_THIS_SCRIPT}/StarRail/components/inGame/zhiyuan.png"
huangquan_path = f"{THE_PATH_OF_THIS_SCRIPT}/StarRail/components/inGame/huangquan.png"
enqueue_path = f"{THE_PATH_OF_THIS_SCRIPT}/StarRail/components/inGame/enqueue.png"
startChallenge_path = f"{THE_PATH_OF_THIS_SCRIPT}/StarRail/components/inGame/startChanllenge.png"
oneMoreTime_path = f"{THE_PATH_OF_THIS_SCRIPT}/StarRail/components/inGame/oneMoreTime.png"
cancel_path = f"{THE_PATH_OF_THIS_SCRIPT}/StarRail/components/inGame/cancel.png"
exitTheGame_path = f"{THE_PATH_OF_THIS_SCRIPT}/StarRail/components/inGame/exitTheGame.png"
adopt_path = f"{THE_PATH_OF_THIS_SCRIPT}/StarRail/components/inGame/adopt.png"
gift_path = f"{THE_PATH_OF_THIS_SCRIPT}/StarRail/components/inGame/gift.png"
clickToClose_path = f"{THE_PATH_OF_THIS_SCRIPT}/StarRail/components/inGame/clickToClose.png"

# 游戏路径
path = THE_PATH_OF_ORIGIN_GAME

# 主函数
DEBUG = True


if DEBUG:
    print("----开始运行------")
    # 运行
    run_the_exe(path)

    # focus_the_exe(path,'崩铁')
    # 登录
    find_and_click_image(clickToLogin_path)
    # 进入手机
    find_image_press_key(phone_path,'esc')

    ClickList_1 = [enTrust_path,getTheEnTrust_path,getTheEnTrustAgain_path,exit_path,zhinan_path,tili1_path,yiqi_path]

    for click in ClickList_1:
        if click == exit_path:
            time.sleep(3)
        find_and_click_image(click)

    find_and_click_right_of_image(yiqi1_path)

    #刷遗器
    ClickList_2 = [challenge_path,zhiyuan_path,huangquan_path,enqueue_path,startChallenge_path]

    for click in ClickList_2:
        find_and_click_image(click)

    while True:
        time.sleep(1)

        find_and_click_image_once(oneMoreTime_path)
        if find_and_click_image_once(cancel_path):
            find_and_click_image(exitTheGame_path)
            break

    find_and_click_image(exit_path)

    find_image_press_key(phone_path, 'esc')

    find_and_click_image(zhinan_path)

    i = 0

    while i < 5:
        time.sleep(1)

        find_and_click_image_once(adopt_path)

        i += 1
    i = 0

    while i < 5:
        time.sleep(1)

        find_and_click_image_once(gift_path)

        time.sleep(0.5)

        find_and_click_image_once(clickToClose_path)

        i += 1

else:
    focus_the_exe(path)
