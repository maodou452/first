# -*- coding: utf-8 -*-
"""
猜数字小游戏
1. 电脑随机生成一个 1~100 的数字
2. 用户不断输入猜测的数字
3. 电脑提示 "大了" 或 "小了"
4. 猜中后告诉用户一共猜了几次
"""

import random  # 导入随机数模块

# 电脑随机出一个 1~100 的整数（含 1 和 100）
answer = random.randint(1, 100)

print("我想好了一个 1~100 之间的整数，你来猜猜看吧！")

count = 0  # 记录用户猜了多少次

while True:
    # 读取用户输入，并转成整数
    guess = int(input("请输入你猜的数字："))
    count += 1  # 每猜一次，次数加 1

    if guess > answer:
        print("大了")
    elif guess < answer:
        print("小了")
    else:
        # 相等就是猜中了，结束循环
        print(f"恭喜你猜对了！答案就是 {answer}")
        print(f"你一共猜了 {count} 次")
        break
