import random

# 题目要求：编写一个程序，随机生成一个1到100之间的整数，然后要求用户猜这个数字是多少。

secret_number = random.randint(1, 100)

print("猜数字游戏！我已经生成了一个1到100之间的随机整数。")

while True:
    guess = int(input("请猜一个数字："))
    
    if guess == secret_number:
        print("恭喜你猜对了！")
        break
    else:
        print("猜错了！")

# 练习：编写一个程序，随机生成一个1到100之间的整数，然后要求用户猜这个数字是多少。如果用户猜错了，程序会提示他猜大了还是猜小了，直到用户猜对为止。
