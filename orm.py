# coding=utf8

from peewee import CharField, IntegerField, Model, FloatField, MySQLDatabase
from peewee import TextField, DateTimeField
from playhouse.shortcuts import model_to_dict


my_database = MySQLDatabase(host='127.0.0.1', user='root', passwd='123456',
                            database='task_manage')
my_database.connect()


class MyBaseModel(Model):
    class Meta:
        global my_database
        database = my_database


class user(MyBaseModel):
    userID = CharField()
    userName = CharField()
    userPass = CharField()
    isBoss = IntegerField()  # 1表示是学长，０表示不是
    taskNowTime = IntegerField()
    taskFinished = IntegerField()
    mainID = CharField()   # 以字符串形式存储，“[id1,id2,id3]”
    childID = CharField()


class main_task(MyBaseModel):
    name = CharField()
    leader = CharField()
    member = CharField()    # 以字符串形式存储，“[id1,id2,id3]”
    totalWeight = IntegerField()
    childTask = CharField()    # 以字符串形式存储，“[id1,id2,id3]”
    startTime = DateTimeField()
    endTime = DateTimeField()
    describe = TextField()


class child_task(MyBaseModel):
    name = CharField()
    mainTask = CharField()   # 存储大任务的名字
    person = CharField()     # 子任务负责人
    childWeight = IntegerField()
    status = IntegerField()    # 1表示完成，０表示未完成
    startTime = DateTimeField()
    endTime = DateTimeField()
    describe = TextField()


# user_data = [
#     {"userID": "1", "userName": "赵振华", "userPass": "e10adc3949ba59abbe56e057f20f883e", "isBoss": 1,
#      "taskNowTime": 0, "taskFinished": 0, "mainID": "", "childID": ""},
#     {"userID": "2", "userName": "陈飞坤", "userPass": "e10adc3949ba59abbe56e057f20f883e", "isBoss": 0,
#      "taskNowTime": 0, "taskFinished": 0, "mainID": "", "childID": ""},
#     {"userID": "3", "userName": "刘文健", "userPass": "e10adc3949ba59abbe56e057f20f883e", "isBoss": 0,
#      "taskNowTime": 0, "taskFinished": 0, "mainID": "", "childID": ""},
#     {"userID": "4", "userName": "周桐", "userPass": "e10adc3949ba59abbe56e057f20f883e", "isBoss": 0,
#      "taskNowTime": 0, "taskFinished": 0, "mainID": "", "childID": ""},
#     {"userID": "5", "userName": "吴炜锋", "userPass": "e10adc3949ba59abbe56e057f20f883e", "isBoss": 0,
#      "taskNowTime": 0, "taskFinished": 0, "mainID": "", "childID": ""},
#     {"userID": "6", "userName": "姜金霖", "userPass": "e10adc3949ba59abbe56e057f20f883e", "isBoss": 0,
#      "taskNowTime": 0, "taskFinished": 0, "mainID": "", "childID": ""},
#     {"userID": "7", "userName": "彭一", "userPass": "e10adc3949ba59abbe56e057f20f883e", "isBoss": 0,
#      "taskNowTime": 0, "taskFinished": 0, "mainID": "", "childID": ""},
#     {"userID": "8", "userName": "江宇川", "userPass": "e10adc3949ba59abbe56e057f20f883e", "isBoss": 0,
#      "taskNowTime": 0, "taskFinished": 0, "mainID": "", "childID": ""},
#     {"userID": "9", "userName": "兰子柠", "userPass": "e10adc3949ba59abbe56e057f20f883e", "isBoss": 0,
#      "taskNowTime": 0, "taskFinished": 0, "mainID": "", "childID": ""},
#     {"userID": "10", "userName": "王心雨", "userPass": "e10adc3949ba59abbe56e057f20f883e", "isBoss": 0,
#      "taskNowTime": 0, "taskFinished": 0, "mainID": "", "childID": ""}
# ]
# with my_database.atomic():
#     user.insert_many(user_data).execute()

# my_database.create_tables([user, main_task, child_task], safe=True)      # 第一次运行使用
# my_database.close()
# print("mysql success!!")