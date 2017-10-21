# -*- coding: utf-8 -*-
from api_define import login_in
from orm import user, model_to_dict
import hashlib


class LoginIn(login_in):
    """
    处理登录请求

    { ‘status’：1/2/3   #学长是1，学生是2,验证失败是3}
    """
    def entry(self, request):
        # body = ast.literal_eval(request.request.body)
        # user_name = str(body["name"])
        # user_pass = str(body["pass"])
        try:
            user_name = request.get_argument("name")
            user_pass = request.get_argument("pass")
            return self.get_user(user_name, user_pass)
        except:
            return {"status": 3}

    def get_user(self, user_name, user_pass):
        user_data = user.select(user.userPass, user.isBoss).where(
            user.userName == user_name)
        if not user_data:
            return {"status": 3}
        else:
            md5 = hashlib.md5()
            data = model_to_dict(user_data[0])
            md5.update(user_pass.encode('utf-8'))
            password = md5.hexdigest()
            if password != data["userPass"]:
                return {"status": 3}
            else:
                if data["isBoss"]:
                    return {"status": 1}
                return {"status": 2}
