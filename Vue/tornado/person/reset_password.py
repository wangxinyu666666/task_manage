# -*- coding: utf-8 -*-
from api_define import reset_password
from orm import user
import ast
import hashlib


class ResetPassword(reset_password):
    """
    重置密码
    POST
    接收数据
    {
        "name": "xxx",
        "old_pass": "xxxxx",
        "new_pass": "xxxxx"
    }
    
    返回数据
    成功{"info": "success"}
    失败{"info": "error"}
    """
    def entry(self, request):
        data = request.request.body.decode()
        data = ast.literal_eval(data)
        return self.reset_pass(data)

    def reset_pass(self, data):
        try:
            name = data["name"]
            old_pass = data["old_pass"]
            new_pass = data["new_pass"]
        except KeyError:
            return {"info": "error"}
        hashed_old = hashlib.new("md5", old_pass.encode('utf-8')).hexdigest()
        user_data = user.select(user.userPass).where(user.userName == name)
        if hashed_old != user_data[0].userPass:
            return {"info": "error"}
        hashed_new = hashlib.new("md5", new_pass.encode('utf-8')).hexdigest()
        user.update(**{"userPass": hashed_new}).where(user.userName == name).execute()
        return {"info": "success"}


