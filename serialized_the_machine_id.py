# -*- coding: UTF-8 -*-
# This module aims at make a sort for the machine ids, which will be load from other files.
from collections import OrderedDict


def print_cnt(dic, path):  # 写入函数模块
    with open(path, 'w') as f:
        for key in dic:
            f.write(key + ',' + str(dic[key]) + '\n')
        f.close()


if __name__ == '__main__':  # 主函数模块
    submit, result, medium, finish = {}, {}, {}, {}
    number = 0
    with open('F:/谷歌数据/machine_id.txt', 'r') as f:  # 读取事先写好的文件，其中包含一些有用的信息
        for line in f:
            temp = line.replace('\n', '').split(',')  # 对将要读取的文件进行按逗号的分割
            machine_id = temp[0]
            submit[machine_id] = 1  # 赋予字典以权值
        f.close()
    result = OrderedDict(sorted(submit.items(), key=lambda d: int(d[0])))  # 调用函数库来实现对字典的排序操作，按key排序
    with open('F:/谷歌数据/construct_第二十九天.txt', 'r') as f:
        for line in f:
            temp = line.replace('\n', '').split(',')
            machine_id = temp[0]
            if machine_id == '':  # 跳过读取的内容中包含空字符串的问题
                number += 1
                continue
            if machine_id not in medium:
                medium[machine_id] = float(temp[1])
        f.close()
    for key in result:
        if key in medium:
            finish[key] = medium[key]
        else:
            finish[key] = 0
    print_cnt(finish, 'E:/谷歌数据/machine_ratio_29.txt')  # 写入文件操作
    print(number)
