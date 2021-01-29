# Google_cluster
关于绘制热力图的步骤说明：


new_i（i：0~29）文件有四列，分别表示job_id,task_index,the number of submit,the number of fail. 
new_i（i：0~29）文件的生成是通过遍历task_events众多文件，将其中的job_id和task_index共同作为每个任务的ID，当做字典的key，并遍历task_events统计每个key的submit和fail个数。

