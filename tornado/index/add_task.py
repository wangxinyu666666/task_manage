from api_define import add_task
from orm import user, main_task, model_to_dict
import ast


class AddTask(add_task):
    """
    首页里发布新任务请求
    {
        "mydata": {
          "name": "",
          "date1": "",
          "date2": "2017-2-1",
          "leader":"xxx",
          "member": ["陈飞坤", "彭一"],
          "goal": "100%",//目标百分比
          "desc": "asdasddf"//需求描述
        }
    }
    """
    def entry(self, request):
        # data = request.get_argument("mydata")
        # data = ast.literal_eval(request.request.body)
        if request.request.body:
            data = request.request.body.decode()
            data = ast.literal_eval(data)
            return self.add_task(data["mydata"])
        return {"result": "mistake"}

    def add_task(self, data):
        # 将组员名字转换为id
        exist = main_task.select(main_task.id).where(main_task.name == data["name"])
        if exist:
            return {"info": "task already exist"}
        leader = user.select(user.userName).where(
            user.userName == data["leader"])
        if not leader:
            return {"result": "mistake"}
        member_ids = []
        members = data["member"]
        for name in data["member"]:
            # 将名字转换为id
            user_data = user.select(user.id).where(
                user.userName == name)
            member_ids.append(user_data[0].id)
        data["member"] = str(member_ids)
        data["goal"] = int(data["goal"][:-1])
        main_task.create(**{"name": data["name"], "leader": data["leader"],
                            "member": data["member"], "childTask": "",
                            "totalWeight": data["goal"],
                            "startTime": data["date1"],
                            "endTime": data["date2"],
                            "describe": data["desc"]})
        # 将main_task的Id加入每个组员的数据库中
        main_id = main_task.select(main_task.id).where(main_task.name == data["name"])
        main_id = model_to_dict(main_id[0])
        for name in members:
            task = user.select(user.mainID).where(user.userName == name)
            task = model_to_dict(task[0])
            if task["mainID"] == "":
                ID = [main_id["id"]]
                ID = str(ID)
            else:
                ID = ast.literal_eval(task["mainID"])
                ID.append(main_id["id"])
                ID = str(ID)
            user.update(**{"mainID": ID}).where(user.userName == name).execute()
        # 将main_task的ID加入组长的数据库中
        lead_main_id = user.select(user.mainID).where(user.userName == data["leader"])
        lead_main_id = model_to_dict(lead_main_id[0])
        if lead_main_id["mainID"] == "":
            lead_main_id["mainID"] = [main_id["id"]]
        else:
            lead_main_id["mainID"] = ast.literal_eval(lead_main_id["mainID"])
            lead_main_id["mainID"].append(main_id["id"])
        lead_main_id["mainID"] = str(lead_main_id["mainID"])
        user.update(**{"mainID": lead_main_id["mainID"]}).where(user.userName == data["leader"]).execute()
        return {"result": "success"}
