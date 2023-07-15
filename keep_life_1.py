import random

# 生成随机数
target_number = random.randint(1, 100)

# 初始化猜测次数
guesses_taken = 0

print("欢迎参加猜数字游戏！")

while True:
    # 获取用户输入
    guess = int(input("请输入你猜测的数字："))

    # 增加猜测次数
    guesses_taken += 1

    # 判断猜测结果
    if guess < target_number:
        print("太小了！再试一次。")
    elif guess > target_number:
        print("太大了！再试一次。")
    else:
        print(f"恭喜你，猜对了！你一共猜了 {guesses_taken} 次。")
        break
