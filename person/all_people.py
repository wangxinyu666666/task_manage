# -*- coding: utf-8 -*-
from api_define import all_people
from orm import user, model_to_dict
import json


class AllPeople(all_people):
    """
    处理所有成员概览页面请求
    数据格式：
    {
        "tableData": [{
            "name": "xxx",
            "doing": "20%"
            "done": "30%"
        },
        {
            "name": "xxx",
            "doing": "20%"
            "done": "30%"
        }]
    }
    """

    def entry(self, request):
        return self.get_data()

    def get_data(self):
        user_data = user.select(user.userName, user.taskNowTime,
                                user.taskFinished)
        table_data = []
        for data in user_data:
            data = model_to_dict(data)
            data["taskNowTime"] = str(data["taskNowTime"]) + "%"
            data["taskFinished"] = str(data["taskFinished"]) + "%"
            table_data.append({"name": str(data["userName"]),
                               "doing": str(data["taskNowTime"]),
                               "done": str(data["taskFinished"])})

        return json.dumps({"tableData": table_data}, ensure_ascii=False)

