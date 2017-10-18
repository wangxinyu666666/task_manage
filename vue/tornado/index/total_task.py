from api_define import total_task
from orm import main_task
import datetime
import json
from peewee import MySQLDatabase


class TotalTask(total_task):
    """
    处理主页下任务概览的请求
    {"AllTask":[{
    "taskname":"实验室任务管理",
    "name":"彭一",
    "start":"2017-9-14",
    "end":"2017-10-14",
    "state":"未完成",
    "percent":"100%"
    },
    {
      "taskname":"实验室任务管理",
      "name":"彭一",
      "start":"2017-9-14",
      "end":"2017-10-14",
      "state":"未完成",
      "percent":"100%"
    }}
    
    """
    def entry(self, request):
        # 权限管理，未完成
        return self.get_data()

    def get_data(self):
        data_list = []
        tasks = main_task.select(
            main_task.name, main_task.leader, main_task.startTime,
            main_task.endTime, main_task.totalWeight)
        for task in tasks:
            end_time = str(task.endTime.date()).split('-')
            endtime = datetime.datetime(int(end_time[0]), int(end_time[1]),
                                        int(end_time[2]))
            nowtime = datetime.datetime.now()
            status = (endtime - nowtime).days
            task.startTime = str(task.startTime.date())
            task.endTime = str(task.endTime.date())
            task.totalWeight = str(task.totalWeight) + "%"
            data_list.append({"taskname": task.name, "name": task.leader,
                              "start": task.startTime, "end": task.endTime,
                              "state": int(status),
                              "percent": task.totalWeight})
        return json.dumps({"AllTask": data_list}, ensure_ascii=False)
        