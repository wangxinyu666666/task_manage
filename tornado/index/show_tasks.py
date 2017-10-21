# -*- coding: utf-8 -*-
from api_define import show_tasks
from orm import my_database, user, main_task, child_task, model_to_dict
import json
import ast


class ShowTasks(show_tasks):
    """
    {
        "start":"2017-9-10",
        "end":"2017-10-23",
        "actor":"彭一",
        "groPeo":["陈飞坤", "王心雨"],
        "desc":"发我计费发到您就能吃饭",
        "TaskDetail":[{
        "misname":"任务一",
        "mispeo":"彭一",
        "misper":"10",
        "miscon":"完成",
        "misend":"",
        "misdetail":"djieigjirejferfjweijmcwejdchfmdkmcfdjkcferncufircghfhcgrurghueghjieriojgjoiiojgeoreoijejifeiojfieomcfjldfjdjckdfjfdjfkecnur"
        }]
    }
    """
    def entry(self, request):
        try:
            task_name = request.get_argument("task")
            return self.get_data(task_name)
        except:
            return {"info": "missing argument"}

    def get_data(self, task_name):
        try:
            task = main_task.select(main_task.startTime, main_task.endTime,
                                    main_task.leader, main_task.member,
                                    main_task.describe,
                                    main_task.childTask).where(
                                        main_task.name == task_name)
            if not task:
                return {"info": "no such task"}
            task[0].startTime = task[0].startTime.date()
            task[0].endTime = task[0].endTime.date()
            # 将成员Id转换为名字
            members = []
            task[0].member = ast.literal_eval(task[0].member)
            for member_id in task[0].member:
                member = user.select(user.userName).where(user.id == member_id)
                members.append(str(member[0].userName))
            task = model_to_dict(task[0])

            # 将子任务id转换为详情
            task_detail = []
            if task["childTask"] != "":
                task["childTask"] = ast.literal_eval(task["childTask"])
                for task_id in task["childTask"]:
                    sub_task = child_task.select(child_task.name, child_task.person,
                        child_task.childWeight, child_task.status,
                        child_task.endTime, child_task.describe).where(child_task.id == task_id)
                    sub_task[0].endTime = sub_task[0].endTime.date()
                    sub_task = model_to_dict(sub_task[0])
                    sub_task["status"] = "完成" if sub_task["status"] == 1 else "未完成"
                    task_detail.append({"misname": sub_task["name"],
                        "mispeo": sub_task["person"], "misper": sub_task["childWeight"],
                        "miscon": sub_task["status"], "misend": str(sub_task["endTime"]),
                        "misdetail": sub_task["describe"]})
                
            data = {"start": str(task["startTime"]), "end": str(task["endTime"]),
                    "actor": task["leader"], "groPeo": members,
                    "desc": task["describe"], "TaskDetail": task_detail}
            return json.dumps(data, ensure_ascii=False)
        except Exception as e:
            print(e)
            return {"info": "database error"}
