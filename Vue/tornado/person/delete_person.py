# -*- coding: utf-8 -*-
from api_define import delete_person
from orm import user
import ast


class DeletePerson(delete_person):
    """
    冻结成员
    POST
    接收数据{"name": "xxxx"}

    返回数据
    成功：{"info": "success"}
    失败：{"info": "error"}
    """
    def entry(self, request):
        data = request.request.body.decode()
        data = ast.literal_eval(data)
        return self.reset_data(data)

    def reset_data(self, data):
        try:
            name = data["name"]
        except KeyError:
            return {"info": "error"}
        user.update(**{"userPass": "deleted", "isBoss": 2}) \
            .where(user.userName == name).execute()
        return {"info": "success"}