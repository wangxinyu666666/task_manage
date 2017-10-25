# -*- coding: utf-8 -*-
from api_define import add_person
from orm import user
import ast
import hashlib


class AddPerson(add_person):
    '''
    增加成员
    接收数据：
    {"name": "xxx",
     "pswd": "xxxxxx"}
    
    返回数据：
    成功时{"info": "success"}
    失败时{"info": "error"}
    '''
    def entry(self, request):
        data = request.request.body.decode()
        data = ast.literal_eval(data)
        return self.add_user(data)

    def add_user(self, data):
        try:
            name = data["name"]
            password = data["pswd"]
        except KeyError:
            return {"info": "error"}
        user_data = user.select().where(user.userName == name, user.isBoss == 0)
        if user_data:
            return {"info": "already exist"}
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        hashed_password = md5.hexdigest()
        user.create(**{"userID": "", "userName": name, "userPass": hashed_password,
                       "isBoss": 0, "taskNowTime": 0, "taskFinished": 0,
                       "mainID": "", "childID": ""})
        user_id = user.select(user.id).where(user.userName == name, user.isBoss == 0)
        user.update(**{"userID": user_id[0].id}).where(user.userName == name).execute()
        return {"info": "success"}
