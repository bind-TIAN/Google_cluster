# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import math


def function(File_name, All_task, Duration):  # 第一个代表文件名，第二个代表计数变量，最后一个代表新列表
    with open(File_name, 'r') as f:  # 读文件
        for line in f:
            temp = line.replace('\n', '').split(',')  # 对文件进行处理
            All_task += 1
            if float(temp[2]) < 1000:  # 对切片时间区间进行规定
                Duration[math.floor(float(temp[2]) / float(2))] += 1  # 用整除将0-1000分为500段
        f.close()
    Duration = np.cumsum(Duration)  # 求累加
    return All_task, Duration


if __name__ == '__main__':
    duration_1, duration_2, duration_3, duration_4 = [0] * 500, [0] * 500, [0] * 500, [0] * 500
    # all_task_0\1\2\3 = 0  # 统计总数，用来计算比例
    all_task_0, duration_1 = function('G:/实习文件夹/绘图python包/schedule_priority/schedule_0.txt', 0, duration_1)  # 打开文件代码
    all_task_1, duration_2 = function('G:/实习文件夹/绘图python包/schedule_priority/schedule_1.txt', 0, duration_2)  # 第一个参数是文件名
    all_task_2, duration_3 = function('G:/实习文件夹/绘图python包/schedule_priority/schedule_2.txt', 0,
                                      duration_3)  # 第二个参数是计数变量，初始化为0
    all_task_3, duration_4 = function('G:/实习文件夹/绘图python包/schedule_priority/schedule_3.txt', 0,
                                      duration_4)  # 最后一个代表要生成的列表，用于后续遍历
    # 以2秒进行切片分析，分析区间是0秒到1000秒，由于这部分的事件时间占多数，因此价值比较大。
    plt.plot([math.log10(i + 1) for i in range(0, 1000, 2)], [math.log10(j) for j in duration_1], label='schedule_0')
    plt.plot([math.log10(i + 1) for i in range(0, 1000, 2)], [math.log10(j) for j in duration_2], label='schedule_1')
    plt.plot([math.log10(i + 1) for i in range(0, 1000, 2)], [math.log10(j) for j in duration_3], label='schedule_2')
    plt.plot([math.log10(i + 1) for i in range(0, 1000, 2)], [math.log10(j) for j in duration_4], label='schedule_3')
    plt.legend()  # 生成图形
    plt.xlabel('Scheduling time(x=lg(time))')
    plt.ylabel('Numbers of tasks(y=lg(numbers_of_tasks))')
    plt.show()