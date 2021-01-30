# -*- coding: UTF-8 -*-
# 统计调度类与submit/evict/fail/finish/kill之间的关系
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

name_list = ['0', '1', '2', '3', '']  # 堆积柱状图的横坐标
# 堆积柱状图的数据，代表着任务类型比例与调度类的关系
num_list_0 = [0.058684443441051275, 0.0947013067005644, 0.0409363161315135, 0.0801706774596932, 0]
num_list_1 = [0.15973950620003977, 0.11759646226134197, 0.046736765806827354, 0.22255080709056024, 0]
num_list_2 = [0.20356399794017513, 0.23448288328437406, 0.0229078105747842, 0.00011454863066657757, 0]
num_list_3 = [0.07906138306900995, 0.052205093629402906, 0.38814445605190406, 0.18199868269074734, 0]
num_list_4 = [0.4989506693497239, 0.5010142541243167, 0.5012746514349709, 0.5151652841283326, 0]
# 绘制堆积柱状图的方法
num_01 = [num_list_0[i] + num_list_1[i] for i in range(0, 5)]
num_012 = [num_list_0[i] + num_list_1[i] + num_list_2[i] for i in range(0, 5)]
num_0123 = [num_list_0[i] + num_list_1[i] + num_list_2[i] + num_list_3[i] for i in range(0, 5)]
# width代表图形宽度，color代表颜色，label代表标签
plt.bar(name_list, num_list_0, width=0.4, align="center", color="#FF6347", tick_label=["0", "1", "2", "3", ""],
        label="evict")
plt.bar(name_list, num_list_1, width=0.4, align="center", bottom=num_list_0, color="#ADFF2F", label="fail")
plt.bar(name_list, num_list_2, width=0.4, align="center", bottom=num_01, color="#ADD8E6", label="finish")
plt.bar(name_list, num_list_3, width=0.4, align="center", bottom=num_012, color="#EE82EE", label="kill")
plt.bar(name_list, num_list_4, width=0.4, align="center", bottom=num_0123, color="#00CED1", label="submit")
# 绘制并展示图片
plt.xlabel("Schedule class")
plt.ylabel("Task type event ratio")
plt.legend()
plt.show()
