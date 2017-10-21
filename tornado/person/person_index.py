import ast
import json
from api_define import person_index
from orm import user, main_task, child_task, model_to_dict


class PersonIndex(person_index):
    """
    个人页
    {"MyTask":[{
      "project":"实验室任务管理",
      "actor":"组长",
      "OnePer":"60%"
    }],
    "percent":"60%"
    }

    """
    def entry(self, request):
        try:
            name = request.get_argument("name")
            return self.get_data(name)
        except:
            return {"error": "missing argument"}

    def get_data(self, name):
        user_data = user.select(user.mainID, user.taskFinished, user.childID) \
                        .where(user.userName == name)
        user_data = model_to_dict(user_data[0])
        if user_data["childID"] == "":
            user_data["childID"] = []
        else:
            user_data["childID"] = ast.literal_eval(user_data["childID"])
        if user_data["mainID"] == "":
            user_data["mainID"] = []
        else:
            user_data["mainID"] = ast.literal_eval(user_data["mainID"])
        tasks = []
        for main_id in user_data["mainID"]:
            task = main_task.select(main_task.name, main_task.leader, main_task.childTask) \
                            .where(main_task.id == main_id)
            task = model_to_dict(task[0])
            if task["childTask"] == "":
                task["childTask"] = []
            else:
                task["childTask"] = ast.literal_eval(task["childTask"])
            percen = 0
            for ID in task["childTask"]:
                if ID in user_data["childID"]:
                    sub_task = child_task.select(child_task.childWeight).where(child_task.id == ID)
                    percen += int(sub_task[0].childWeight)
            percen = str(percen) + "%"
            tasks.append({"project": task["name"], "actor": task["leader"],
                          "OnePer": percen})

        percent = str(user_data["taskFinished"]) + "%"

        return json.dumps({"MyTask": tasks, "percent": percent}, ensure_ascii=False)
    