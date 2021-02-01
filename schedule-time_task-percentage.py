# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import math
import numpy as np


def function(File_name, Dict):  # 第一个参数表示传递文件名，第二个参数表示生成的新字典
    with open(File_name, 'r') as f:
        for line in f:
            temp = line.replace('\n', '').split(',')
            task_id = temp[0] + ',' + temp[1]  # 给新字典赋予键值
            if task_id not in Dict:
                Dict[task_id] = float(float(temp[3]) / 1000000)  # 转换成s
        f.close()


if __name__ == '__main__':
    duration = [0] * 500  # 初始化一个空列表
    dict = {}  # 初始化一个空字典
    all_task = 0  # 计数变量初始化为0
    function('task_schedule_time_with_timestamp.txt', dict)  # 调用函数获得新字典
    with open('all.txt', 'w') as f:  # 打开文件进行写入操作
        for key in dict:
            f.write(key + ',' + str(dict[key]) + '\n')
        f.close()
    with open('all.txt', 'r') as f:  # 再次打开刚才写入的文件，读取文件
        for line in f:
            temp = line.replace('\n', '').split(',')
            all_task += 1
            if float(temp[2]) < 1000:  # 判断是否在1000s内
                duration[math.floor(float(temp[2]) / float(2))] += 1  # 用整除将0-1000分为500段
    duration = np.cumsum(duration)  # 求累加
    plt.plot([i for i in range(0, 1000, 2)], [float(j / all_task) for j in duration])  # 将0-1000切分成500段并求出每一段的值不断进行叠加
    plt.xlabel('Scheduling time(s)')
    plt.ylabel('Percentage of tasks(100%)')
    plt.show()
