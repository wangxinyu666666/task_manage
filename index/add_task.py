from api_define import add_task
from orm import user, main_task
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
          "member":"陈飞坤，彭一",
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
        leader = user.select(user.userName).where(
            user.userName == data["leader"])
        if not leader:
            return {"result": "mistake"}
        member_ids = []
        member_names = data["member"].split("，")
        for name in member_names:
            user_data = user.select(user.userID).where(
                user.userName == name)
            if not user_data:
                return {"result": "mistake"}
            member_ids.append(user_data[0].userID)
        data["member"] = str(member_ids)
        data["goal"] = int(data["goal"][:-1])
        main_task.create(**{"name": data["name"], "leader": data["leader"],
                            "member": data["member"], "totalWeight": data["goal"],
                            "childTask": "", "startTime": data["date1"],
                            "endTime": data["date2"], "describe": data["desc"]})
        return {"result": "success"}
        

