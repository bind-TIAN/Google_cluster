## 关于绘制热力图的步骤说明：
---
### new_i（i：0~29）文件有四列，其文件的生成是通过以下步骤实现。
---
*    第一步：遍历task_events众多文件，将其中的job_id和task_index共同作为每个任务的ID，当做字典的key。
*    第二步：按照每一天（总共二十九天）时间段遍历task_events统计属于每个时间段的每个key的submit和fail个数。
*    第三步：文件的每一列分别有job_id，任务的index，以及属于每个key的提交和失败的个数，所有这些信息都是从task_event众多文件中得出的。（给出了一个new_1.txt作为文件事例）

### 修改相应文件以得到更新后的热力图绘制效果
---
*    按照code中的write open以及read open中的内容对文件名进行修改和相应文件的个数的扩充（有的文件有二十九个，分别命名到指定文件夹下）即可以得出绘制的热力图。

## 关于构建task_schedule_time_with_timestamp.txt文件说明：
---
*    读取task_events众多文件，得出需要用的由job_id和task_index共同组成的表征每个任务ID的字段，相应的调度时间，调度类和优先级。
*    job_id,task_index,timestamp,schedule_time,schedule_class,priority

## 关于构建图表：
*    Figure_ratio_with_priority.png：优先级与任务类型事件比率堆积直方图。
*    Figure_schedule_time_with_eventtypes.png：调度类与任务事件比率堆积直方图。
*    Figure_tasks_with_schedule_classes.png：调度时间与任务个数Log-log图。
*    Figure_time_and_machine_numbers.png：时间与事件类型折线图（time_numbers-events.py）。
*    figure-schedule_class_submit_evict_fail_finish_kill.png：调度类与任务事件类型比率堆积柱状图。
*    heat_map_costruct.png：天数与机器个数热力图。


