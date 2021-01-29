# -*- coding: UTF-8 -*-
# Statistics on the first day, the ratio of submit-fail belonging to each machine_id in the first 500 files of task_event.
import gzip


def print_cnt(dic, path):  # 写入文件函数
    with open(path, 'w') as f:
        for key in dic:
            if dic[key][0] == 0:
                symbol = 0
            else:
                symbol = float(dic[key][1]) / float(dic[key][0])  # 除法运算
            f.write(key + ',' + str(symbol) + '\n')
        f.close()


if __name__ == '__main__':  # 主函数
    submit, result = {}, {}  # 初始化两个字典
    with open('F:/谷歌数据/new_12.txt', 'r') as f:
        for line in f:
            temp = line.replace('\n', '').split(',')  # 按行读取，并且用逗号分隔
            task_id = temp[0] + ',' + temp[1]
            if task_id not in submit:
                submit[task_id] = [int(temp[2]), int(temp[3])]  # 必要元素加入字典
        f.close()
    for i in range(0, 500):
        task_file = 'G:/实习文件夹/google_trace数据集/task_events/part-00' + str(i).zfill(3) + '-of-00500.csv.gz'
        print(i)
        with gzip.open(task_file, 'r') as f:
            for line in f:
                temp = str(line, encoding='utf-8').replace('\n', '').split(',')
                task_id = temp[2] + ',' + temp[3]
                if task_id == '':
                    continue  # 若元素为空，直接进行下一轮循环
                if task_id in submit:
                    task_id_two = temp[4]
                    if task_id_two not in result:
                        result[task_id_two] = [submit[task_id][0], submit[task_id][1]]
                    else:
                        result[task_id_two][0] = result[task_id_two][0] + submit[task_id][0]  # 字典对应键值元素累加
                        result[task_id_two][1] = result[task_id_two][1] + submit[task_id][1]
            f.close()
    print_cnt(result, 'F:/谷歌数据/machine_ratio_of_submit_fail_第十二天.txt')  # 写入文件
