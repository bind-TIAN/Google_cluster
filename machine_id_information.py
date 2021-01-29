# -*- coding: UTF-8 -*-
# This module aims at look forward different ids about the machines, and write the machine id into files.
import gzip


def print_cnt(dic, path):  # 打印文件子函数
    with open(path, 'w') as f:
        for key in dic:
            f.write(key + '\n')
        f.close()


if __name__ == '__main__':  # 主函数
    submit, result = {}, {}
    for i in range(0, 500):
        task_file = 'G:/实习文件夹/google_trace数据集/task_events/part-00' + str(i).zfill(3) + '-of-00500.csv.gz'
        print(i)
        with gzip.open(task_file, 'r') as f:  # 打开压缩包
            for line in f:
                temp = str(line, encoding='utf-8').replace('\n', '').split(',')
                task_id = temp[4]
                time = int(temp[0])
                if task_id == '':
                    continue  # 如果字段值为空，则继续下一个循环，跳过当前循环
                if time >= 0 and time < 2505600000000:  # 划定跟踪统计范围
                    if task_id not in submit:
                        submit[task_id] = 1
        f.close()
    print_cnt(submit, 'F:/谷歌数据/machine_id.txt')  # 打印文件的输出函数
