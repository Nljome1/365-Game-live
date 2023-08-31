import random

def guess_number():
    answer = random.randint(1, 100)
    tries = 0
    
    print("猜数字游戏 - 请输入1到100的整数")
    
    while True:
        guess = int(input("请输入你的猜测: "))
        tries += 1
        
        if guess == answer:
            print(f"恭喜你，你猜对了！答案是{answer}。")
            print(f"你一共猜了{tries}次。")
            break
        elif guess < answer:
            print("你的猜测太小了，请继续尝试。")
        else:
            print("你的猜测太大了，请继续尝试。")

guess_number()
