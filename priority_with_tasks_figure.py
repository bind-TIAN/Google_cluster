# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

name_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '']  # 堆积柱状图的横坐标
# 堆积柱状图的数据，代表着任务类型比例与调度类的关系
num_list_0 = [0.2087914711562496, 0.12131371378357811, 0.0386138726686386, 0.12718204488778054, 0.0028497963814402023,
              0,
              0.0006128385315691716, 0, 0.011000546907403805, 0.010490192838736588, 0.01606618116775265, 0, 0]
num_list_1 = [0.4355256624662856, 0.18955231646351975, 0.02140204822827115, 0.0008312551953449709, 0.0421135486146507,
              0,
              0.07773174227670966, 0, 0.0630742068925015, 0.8167361752351643, 0.6842340615817044, 0, 0]
num_list_2 = [0.1431178083796256, 0.4465267762917243, 0.8061093593059921, 0.8204488778054863, 0.7351328622877077, 1,
              0.7247933848291966, 0,
              0.4188282967688417, 0.03066939588335529, 0, 0, 0]
num_list_3 = [0.21256505799783915, 0.24260719346117784, 0.1338747197970981, 0.051537822111388194, 0.21990379271620147,
              0, 0.1968620343625245,
              1, 0.507096949431253, 0.1421042360427439, 0.299699757250543, 1, 0]
# 绘制堆积柱状图的方法
num_01 = [num_list_0[i] + num_list_1[i] for i in range(0, 13)]
num_012 = [num_list_0[i] + num_list_1[i] + num_list_2[i] for i in range(0, 13)]
# width代表图形宽度，color代表颜色，label代表标签
plt.bar(name_list, num_list_0, width=0.4, align="center", color="#FF6347",
        tick_label=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", ""],
        label="evict")
plt.bar(name_list, num_list_1, width=0.4, align="center", bottom=num_list_0, color="#ADFF2F", label="fail")
plt.bar(name_list, num_list_2, width=0.4, align="center", bottom=num_01, color="#ADD8E6", label="finish")
plt.bar(name_list, num_list_3, width=0.4, align="center", bottom=num_012, color="#EE82EE", label="kill")
# 绘制并展示图片
plt.xlabel("Priority")
plt.ylabel("Task type event ratio")
plt.legend()
plt.show()