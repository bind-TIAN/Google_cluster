# -*- coding: UTF-8 -*-
import gzip


def print_res(dic, path):  # 写入文件子函数
    with open(path, 'w') as f:
        for key in dic:
            f.write(key + ',' + str(dic[key]).replace(']', '').replace('[', '').replace(' ', '') + '\n')
        f.close()


if __name__ == '__main__':
    submit, result = {}, {}  # 分别是每个作业的调度时间 和 已经统计过的作业，避免重复统计
    boss, medium = {}, {}
    number = 0
    for i in range(0, 5):
        task_file = 'G:/实习文件夹/google_trace数据集/task_events/part-00' + str(i).zfill(3) + '-of-00500.csv.gz'
        print(i)
        with gzip.open(task_file, 'r') as f:
            for line in f:
                temp = str(line, encoding='utf-8').replace('\n', '').split(',')
                task_id = temp[2] + ',' + temp[3]
                if temp[0] == '0':  # 去除在统计窗口前提交的作业和已经统计过的作业
                    continue
                task_id = temp[2] + ',' + temp[3]
                if temp[5] == '0':
                    submit[task_id] = [int(temp[0]), int(temp[0])]
                if temp[5] == '1':
                    if task_id in submit:
                        if task_id not in medium:
                            medium[task_id] = 1
                        else:
                            medium[task_id] += 1
                        task_id_two = task_id + ',' + str(medium[task_id])
                        boss[task_id_two] = [submit[task_id][0], int(temp[0]) - submit[task_id][1],
                                             int(temp[7]), int(temp[8])]
                        submit.pop(task_id)
            f.close()
    print_res(boss, 'F:/谷歌数据/task_schedule_time_with_timestamp.txt')  # 此时res中就保存着所有有效作业的调度时间
