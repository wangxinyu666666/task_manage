from api_define import task_manage
from orm import user, main_task, child_task, model_to_dict
import json


class TaskManage(task_manage):
    """
    任务管理页面，展示任务信息
    {"start":"2017-9-10",
    "end":"2017-10-23",
    "actor":"彭一",
    "groPeo":"陈飞坤,王心雨",
    "desc":"发我计费发到您就能吃饭",
    "TaskDetail":[{
    "misname":"任务一",
    "mispeo":"彭一",
    "misper":"10",
    "miscon":"完成",
    "misend":"",
    "misdetail": "djieigjirejferfjweijmc"
    }]}
    """
    def entry(self, request):
        # 权限管理，未完成
        try:
            task_name = request.get_argument("xxx")
            return self.get_data(task_name)
        except:
            return {"err": "missing argument"}

    def get_data(self, task_name):
        try:
            tasks = main_task.select(main_task.startTime, main_task.endTime,
                                     main_task.leader, main_task.member,
                                     main_task.describe,
                                     main_task.childTask).where(
                                         task_name == main_task.name)
            # 转换为dict
            tasks[0].startTime = str(tasks[0].startTime.date())
            tasks[0].endTime = str(tasks[0].endTime.date())
            tasks = model_to_dict(tasks[0])
            # 将id转换为组员名字
            members = list(tasks[0].member)
            members_str = ""
            for member_id in members:
                member = user.select(user.userName).where(
                                  user.userID == member_id)
                members_str = members_str + str(member[0].userName) + "，"
            members_str = members_str[:-1]
            # 将id转换为子任务信息
            child_tasks = []
            childs = list(tasks[0].childTask)
            for child_id in childs:
                sub_task = child_task.select(child_task.name,
                                             child_task.person,
                                             child_task.childWeight,
                                             child_task.status,
                                             child_task.endTime,
                                             child_task.describe).where(
                                                 child_id == child_task.id)
                sub_task[0].endTime = str(sub_task[0].endTime.date())
                sub_task = model_to_dict(sub_task[0])
                sub_task["status"] = "完成" if int(sub_task["status"]) else "未完成"
                child_tasks.append({"misname": sub_task["name"],
                                    "mispeo": sub_task["person"],
                                    "miscon": sub_task["status"],
                                    "misend": sub_task["endTime"],
                                    "misdetail": sub_task["describe"]})
            
            result = {"start": tasks["startTime"],
                      "end": tasks["endTime"],
                      "actor": tasks["leader"],
                      "groPeo": members_str,
                      "desc": tasks["describe"],
                      "TaskDetail": child_tasks}
            return json.dumps(result, ensure_ascii=False)

        except:
            return {"err": "databse error"}
