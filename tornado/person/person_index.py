from api_define import person_index
from orm import user, main_task, child_task
import ast


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
        tasks = []
        child_id = (user_data[0].childID)
        main_task_data = main_task.select(main_task.name, main_task.leader,
                                          main_task.childTask)
        if main_task_data:
            for task in main_task_data:
                ids = ast.literal_eval(task.childTask)
                oneper = 0
                for num in ids:
                    if num in child_id:
                        child_task_data = child_task.select(
                            child_task.childWeight).where(child_task.id == num)
                        oneper += int(child_task_data[0].childWeight)
                OnePer = str(oneper) + "%"
                tasks.append({"project": task.name, "actor": task.leader,
                              "OnePer": OnePer})
        else:
            tasks.append({"project": "", "actor": "", "OnePer": ""})

        percent = str(user_data[0].taskFinished) + "%"

        return {"MyTask": tasks, "percent": percent}
    