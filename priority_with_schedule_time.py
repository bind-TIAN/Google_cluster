# -*- coding: UTF-8 -*-
# 统计优先级为i时，每个在1s内、2s内、5s内，1000s内的占比，其中i可取(0~11，temp[5]:0~11)
if __name__ == '__main__':
    submit = {}
    cnt_1, cnt_2, cnt_5, cnt_1000 = 0, 0, 0, 0
    file_name = 'G:/实习文件夹/task_schedule_time_with_timestamp.txt'
    with open(file_name, 'r') as f:
        for line in f:
            temp = line.replace('\n', '').split(',')
            task_id = temp[0] + ',' + temp[1]
            time = int(temp[3])
            if temp[5] == '0' and time < 1000000:
                cnt_1 += 1
            if temp[5] == '0' and time < 2000000:
                cnt_2 += 1
            if temp[5] == '0' and time < 5000000:
                cnt_5 += 1
            if temp[5] == '0' and time > 1000000000:
                cnt_1000 += 1
            if temp[5] == '0':
                if task_id not in submit:
                    submit[task_id] = 1
        f.close()
    length = len(submit)
    print(float(cnt_1) / float(length))
    print(float(cnt_2) / float(length))
    print(float(cnt_5) / float(length))
    print(float(cnt_1000) / float(length))