from api_define import task_manage
from orm import user, main_task, child_task, model_to_dict
import json
import ast


class TaskManage(task_manage):
    """
    任务管理页面，展示任务信息
    {“name”:”实验室任务发布”,
    “leader”:”pengyi”,
    ”starttime”:”2017.9.9”,
    ”endtime”:”2017.09.30”,
    ”perent”:”200%”
    “people”:”陈飞坤，搜索，的”,
    “need”：“1.房间诶广泛SEI加分is2.节节高人跟人3.定界法IE结果位人工及粉丝佛法”
    #sheet先待定。因为有隐藏内容
    “sheet”:[{“mission”:”任务1”,””},
    {},
    {}]
    }
    """
    def entry(self, request):
        # 权限管理，未完成
        return self.get_data()

    def get_data(self):
        tasks = main_task.select(
            main_task.name, main_task.leader, main_task.startTime,
            main_task.endTime, main_task.totalWeight, main_task.childTask,
            main_task.describe, main_task.member)
        data_lists = []
        for task in tasks:
            # 得到所有成员
            members = ""
            ids = ast.literal_eval(task.member)
            for user_id in ids:
                member_name = user.select(user.userName).where(
                    user.userID == user_id)
                members = members + member_name[0].userName + ", "
            members = members[:-1]
            # 得到所有子任务
            child_tasks = []
            child_ids = ast.literal_eval(task.childTask)
            for child_id in child_ids:
                data = child_task.select(
                    child_task.name, child_task.person, child_task.childWeight,
                    child_task.status, child_task.startTime,
                    child_task.endTime, child_task.describe).where(
                        child_task.childID == child_id)
                child_tasks.append(model_to_dict(data))
            data_lists.append({"name": task.name, "leader": task.leader,
                               "starttime": str(task.startTime.date()),
                               "endtime": str(task.endTime.date()),
                               "percent": task.totalWeight, "perple": members,
                               "need": task.describe, "sheet": child_tasks})

        return json.dumps(data_lists, ensure_ascii=False)
