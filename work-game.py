import time

def pomodoro_timer(total_time):
    """实现一个简单的专注时钟，每25分钟工作一次，休息5分钟"""

    print("开始专注时间")

    while total_time > 0:
        # 工作时间25分钟
        work_time = 25 * 60
        while work_time > 0:
            mins, secs = divmod(work_time, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')
            time.sleep(1)
            work_time -= 1
            total_time -= 1

        print("工作结束，休息5分钟")

        # 休息时间5分钟
        rest_time = 5 * 60
        while rest_time > 0:
            mins, secs = divmod(rest_time, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print(timeformat, end='\r')
            time.sleep(1)
            rest_time -= 1
            total_time -= 1

        print("休息结束，开始下一个工作时间")

    print("专注时间结束")
