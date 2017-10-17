from api_define import divide_task
from orm import my_database, user, main_task, child_task, model_to_dict
import json
import ast
import datetime


class DivideTask(divide_task):
    """
    组长划分任务
    "TaskDetail": [{
                    "misname":"任务一",
                    "mispeo":"彭一",
                    "misper":"10",
                    "miscon":"完成",
                    "misend":"",
                    "misdetail": "djieigjirejferfjweijmc"
                   }
                 ]
    """
    def entry(self, request):
        try:
            task_name = request.get_argument("task")
            data = request.request.body.decode()
            data = ast.literal_eval(data)
            return self.update_data(task_name, data["TaskDetail"])
        except:
            return {"err": "missing argument"}

    def update_data(self, task_name, child_data):
        try:
            child_tasks = child_task.select(child_task.person,
                                            child_task.childWeight,
                                            child_task.id,
                                            child_task.status).where(
                                  child_task.mainTask == task_name)
            # 判断是否为第一次插入，如果为第一次直接插入，否则先更改数据库，再删除，最后插入
            if not child_tasks:
                self.insert_data(task_name, child_data)
                return {"info": "insert success"}
            else:
                # 对于修改记录的操作，取出数据库中之前的子任务，依次遍历对user进行修改
                # 修改完后删除子任务，重新插入
                id_list = []
                for child in child_tasks:
                    child = model_to_dict(child)
                    id_list.append(int(child["id"]))
                    # 对user修改
                    user_data = user.select(user.taskNowTime,
                                            user.taskFinished,
                                            user.childID).where(
                                            user.userName == child["person"]
                                            )
                    user_data = model_to_dict(user_data[0])
                    user_data["taskFinished"] = int(user_data["taskFinished"]) - int(child["childWeight"])
                    if not child["status"]:
                        user_data["taskNowTime"] = int(user_data["taskNowTime"]) - int(child["childWeight"])
                    user_data["childID"] = ast.literal_eval(user_data["childID"])
                    user_data["childID"].remove(int(child["id"]))
                    user_data["childID"] = str(user_data["childID"])
                    user.update(**{"taskFinished": user_data["taskFinished"],
                                   "taskNowTime": user_data["taskNowTime"],
                                   "childID": user_data["childID"]}).where(
                                    user.userName == child["person"]).execute()
                # 删除子任务
                child_task.delete().where(child_task.mainTask == task_name).execute()

                self.insert_data(task_name, child_data)
                return {"info": "update success"}

        except Exception as e:
            return {"info": "database error"}

    def insert_data(self, task_name, child_data):
        id_list = []
        for data in child_data:
            data["misend"] = data["misend"][:10]
            data["miscon"] = 1 if data["miscon"] == "完成" else 0
            child_task.create(**{"name": data["misname"],
                                 "mainTask": task_name,
                                 "person": data["mispeo"],
                                 "childWeight": data["misper"],
                                 "status": data["miscon"],
                                 "endTime": data["misend"],
                                 "describe": data["misdetail"],
                                 "startTime": str(datetime.datetime.now())[:10]})
            child_ids = child_task.select(child_task.id).where(
                            child_task.name == data["misname"])
            child_ids = model_to_dict(child_ids[0])
            id_list.append(int(child_ids["id"]))
            user_data = user.select(user.taskNowTime,
                                    user.taskFinished,
                                    user.childID).where(
                        user.userName == data["mispeo"])
            user_data = model_to_dict(user_data[0])
            if user_data["childID"] == "":
                user_data["childID"] = []
            else:
                user_data["childID"] = ast.literal_eval(user_data["childID"])
            user_data["childID"].append(child_ids["id"])
            user_data["childID"] = str(user_data["childID"])
            if not data["miscon"]:
                user_data["taskNowTime"] = int(user_data["taskNowTime"]) + int(data["misper"])
            user_data["taskFinished"] = int(user_data["taskFinished"]) + int(data["misper"])
            user.update(**{"taskFinished": user_data["taskFinished"],
                           "childID": user_data["childID"],
                           "taskNowTime": user_data["taskNowTime"]}
                        ).where(user.userName == data['mispeo']).execute()
                
        main_task.update(**{"childTask": str(id_list)}
                         ).where(main_task.name == task_name).execute()
