# -*- coding: utf-8 -*-
from api_define import get_member
from orm import user, model_to_dict
import json


class GetMember(get_member):
    """
    获取活跃成员
    返回数据
    {
        "member": ["xxx", "zzz", "aaa"]
    }
    """
    def entry(self, request):
        return self.get_data()

    def get_data(self):
        users = user.select(user.userName).where(user.isBoss == 0)
        member = []
        for user_data in users:
            user_data = model_to_dict(user)
            member.append(user_data["userName"])
        return json.dumps({"member": member}, ensure_ascii=False)