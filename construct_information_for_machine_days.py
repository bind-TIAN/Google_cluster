# -*- coding: UTF-8 -*-
# This function aims at construct the information about the ratio of submit and failure, which will include different machines and contiguous days.
def print_cnt(dic, path):  # 打印文件子函数
    with open(path, 'w') as f:
        for key in dic:
            f.write(key + ',' + str(dic[key]) + '\n')
        f.close()


if __name__ == '__main__':  # 主函数
    submit, result, boss = {}, {}, {}  # 初始化一系列字典
    with open('F:/谷歌数据/machine_id.txt', 'r') as f:
        for line in f:
            temp = line.replace('\n', '').split(',')
            machine_id = temp[0]
            submit[machine_id] = 1  # 读取文件中包含的信息，并赋予于字典中，人为设定一个整型数值
        f.close()
    print(len(submit))  # 打印查看字典的长度
    with open('F:/谷歌数据/machine_ratio_of_submit_fail_第二十九天.txt', 'r') as f:
        for line in f:
            temp = line.replace('\n', '').split(',')
            machine_id = temp[0]
            result[machine_id] = float(temp[1])
        f.close()
    for key in submit:  # 遍历字典
        if key not in result:
            boss[key] = 0
        else:
            boss[key] = result[key]
    print_cnt(boss, 'F:/谷歌数据/construct_第二十九天.txt')  # 调用写入文件函数
