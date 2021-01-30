# -*- coding: UTF-8 -*-
import gzip

if __name__ == '__main__':
    a0, b0, c0, d0 = 0, 0, 0, 0
    a1, b1, c1, d1 = 0, 0, 0, 0
    a2, b2, c2, d2 = 0, 0, 0, 0
    a3, b3, c3, d3 = 0, 0, 0, 0
    a4, b4, c4, d4 = 0, 0, 0, 0
    a5, b5, c5, d5 = 0, 0, 0, 0
    a6, b6, c6, d6 = 0, 0, 0, 0
    a7, b7, c7, d7 = 0, 0, 0, 0
    a8, b8, c8, d8 = 0, 0, 0, 0
    a9, b9, c9, d9 = 0, 0, 0, 0
    a10, b10, c10, d10 = 0, 0, 0, 0
    a11, b11, c11, d11 = 0, 0, 0, 0
    for i in range(0, 500):
        task_file = 'G:/实习文件夹/google_trace数据集/task_events/part-00' + str(i).zfill(3) + '-of-00500.csv.gz'
        print(i)
        with gzip.open(task_file, 'r') as f:
            for line in f:
                temp = str(line, encoding='utf-8').replace('\n', '').split(',')
                if temp[0] == '0':
                    continue
                if temp[8] == '6' and temp[5] == '2':
                    a0 = a0 + 1
                if temp[8] == '6' and temp[5] == '3':
                    b0 = b0 + 1
                if temp[8] == '6' and temp[5] == '4':
                    c0 = c0 + 1
                if temp[8] == '6' and temp[5] == '5':
                    d0 = d0 + 1

                if temp[8] == '7' and temp[5] == '2':
                    a1 = a1 + 1
                if temp[8] == '7' and temp[5] == '3':
                    b1 = b1 + 1
                if temp[8] == '7' and temp[5] == '4':
                    c1 = c1 + 1
                if temp[8] == '7' and temp[5] == '5':
                    d1 = d1 + 1

                if temp[8] == '8' and temp[5] == '2':
                    a2 = a2 + 1
                if temp[8] == '8' and temp[5] == '3':
                    b2 = b2 + 1
                if temp[8] == '8' and temp[5] == '4':
                    c2 = c2 + 1
                if temp[8] == '8' and temp[5] == '5':
                    d2 = d2 + 1

                if temp[8] == '9' and temp[5] == '2':
                    a3 = a3 + 1
                if temp[8] == '9' and temp[5] == '3':
                    b3 = b3 + 1
                if temp[8] == '9' and temp[5] == '4':
                    c3 = c3 + 1
                if temp[8] == '9' and temp[5] == '5':
                    d3 = d3 + 1

                if temp[8] == '10' and temp[5] == '2':
                    a4 = a4 + 1
                if temp[8] == '10' and temp[5] == '3':
                    b4 = b4 + 1
                if temp[8] == '10' and temp[5] == '4':
                    c4 = c4 + 1
                if temp[8] == '10' and temp[5] == '5':
                    d4 = d4 + 1

                if temp[8] == '11' and temp[5] == '2':
                    a5 = a5 + 1
                if temp[8] == '11' and temp[5] == '3':
                    b5 = b5 + 1
                if temp[8] == '11' and temp[5] == '4':
                    c5 = c5 + 1
                if temp[8] == '11' and temp[5] == '5':
                    d5 = d5 + 1
        f.close()
    print(a0, b0, c0, d0)
    print(a1, b1, c1, d1)
    print(a2, b2, c2, d2)
    print(a3, b3, c3, d3)
    print(a4, b4, c4, d4)
    print(a5, b5, c5, d5)


