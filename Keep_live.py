import time

# 设置计时器持续时间（单位：秒）
duration = 60

# 获取当前时间
start_time = time.time()

print("计时开始.")

while True:
    # 计算已经过去了多少时间
    elapsed_time = time.time() - start_time

    # 如果已经达到设定的持续时间，则停止计时
    if elapsed_time >= duration:
        print("时间到！")
        break

    # 否则，打印已经过去的时间，并等待1秒
    print("已经过去 {:02d}:{:02d}.".format(int(elapsed_time/60), int(elapsed_time%60)))
    time.sleep(1)
