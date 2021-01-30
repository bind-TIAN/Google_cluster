# -*- coding: UTF-8 -*-
# 统计不同的调度类取值对submit-evict-fail-finish-kill的关系
if __name__ == '__main__':
    submit, result = {}, {}
    number_1, number_2, number_3, number_4, number_5 = 0, 0, 0, 0, 0
    file_name = 'C:/Users/DELL/Desktop/schedule_3.txt'
    with open(file_name, 'r') as f:
        for line in f:
            temp = line.replace('\n', '').split(',')
            task_id = temp[0] + ',' + temp[1]
            if task_id == '':  # 若字段为空，则跳过
                continue
            if task_id not in submit:
                submit[task_id] = 1
        f.close()
    for i in range(0, 500):
        task_file = 'G:/实习文件夹/google_trace数据集/task_events/part-00' + str(i).zfill(3) + '-of-00500.csv.gz'
        print(i)
        with gzip.open(task_file, 'r') as f:
            for line in f:
                temp = str(line, encoding='utf-8').replace('\n', '').split(',')
                task_id_two = temp[2] + ',' + temp[3]
                if task_id_two in submit:
                    if temp[5] == '1':
                        number_1 += 1
                    if temp[5] == '2':
                        number_2 += 1
                    if temp[5] == '3':
                        number_3 += 1
                    if temp[5] == '4':
                        number_4 += 1
                    if temp[5] == '5':
                        number_5 += 1
            f.close()
    print(number_1, number_2, number_3, number_4, number_5)
