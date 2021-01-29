# -*- coding: UTF-8 -*-
# This module aims at reading multifiles to build an array or a matrix to draw a heat map.
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    k = 0
    y = np.random.standard_normal((364965, 2))  # 赋ratio（364965=12585*29）
    z = np.random.standard_normal((364965, 2))  # 赋天数和machine_id
    for i in range(0, 29):
        file_name = 'E:/谷歌数据/machine_ratio_' + str(i + 1) + '.txt'
        count = 0
        with open(file_name, 'r') as f:
            for line in f:
                temp = line.replace('\n', '').split(',')
                count += 1
                y[k][0] = 1  # 该值是谁并不重要
                y[k][1] = float(temp[1])
                z[k][0] = i + 1  # 横坐标表示天数
                z[k][1] = count  # 纵坐标表示第几个machine_id(从0开始编号)
                k += 1
            f.close()
    c = y[:, 1]  # 仅需要y中某一个column的一系列值
    plt.scatter(z[:, 0], z[:, 1], c=c, s=10, marker='.', cmap='Greens')  # 设置区间、颜色、以及绘制的散点的形状大小
    plt.colorbar()  # 添加绘制的颜色色条，直观展示
    plt.show()  # 绘制图形
