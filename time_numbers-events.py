# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import math
def time_check(str):  # 以五分钟为时间切片
    return math.floor(float(str) / (1000000 * 3600 * 24))
if __name__ == '__main__':
    list, list2, list3, list4 = [0 for row in range(30)], [0 for row in range(30)], [0 for row in
                                                                                     range(30)], []  # 列表初始化
    with open('G:/实习文件夹/google_trace数据集/machine_events/part-00000-of-00001.csv', 'r') as f:
        for line in f:
            temp = line.replace('\n', '').split(',')
            if temp[0] == '0':
                continue
            time = time_check(temp[0])  # 返回微秒转秒的结果
            if temp[2] == '0':  # 有三个字段，其中0代表add字段
                list[time] = list[time] + 1
            elif temp[2] == '1':  # 1代表remove字段
                list2[time] = list2[time] + 1
            else:  # 这里应该为2代表update字段
                list3[time] = list3[time] + 1
        f.close()
    del (list[-1])  # 清空列表最后一个元素
    del (list2[-1])
    del (list3[-1])
    for i in range(1, 30):  # 初始化一个空的列表
        list4.append(i)
    plt.xlabel('Time(Day)')  # 绘制折线图，设置横轴标签
    plt.ylabel('Number of events')  # 设置纵轴标签
    plt.plot(list4, list, '--.', color='gray', linewidth=1, label='add')  # add
    plt.plot(list4, list2, '-.*', color='blue', linewidth=1, label='remove')  # remove
    plt.plot(list4, list3, '-v', color='#d725de', linewidth=1, label='update')  # update
    plt.legend()  # 展示图形
    plt.show()