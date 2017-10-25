import tornado.web
import tornado.ioloop
from login.login_in import LoginIn
from index.total_task import TotalTask
from index.add_task import AddTask
from index.divide_task import DivideTask
from index.task_manage import TaskManage
from index.member_manage import MemberManage
from index.show_tasks import ShowTasks
from index.get_member import GetMember
from person.person_index import PersonIndex
from person.all_people import AllPeople
from person.add_person import AddPerson
from person.delete_person import DeletePerson
from person.reset_password import ResetPassword
from peewee import MySQLDatabase


class BaseHandler(tornado.web.RequestHandler):
    '''
    所有Handler的父类
    定义数据库的连接与关闭
    '''

    def prepare(self):
        self.my_database = MySQLDatabase(host='127.0.0.1', user='root', passwd='123456',
                                         database='task_manage')
        self.my_database.connect()
        return super(BaseHandler, self).prepare()

    def on_finish(self):
        if not self.my_database.is_closed():
            self.my_database.close()
        return super(BaseHandler, self).on_finish()


class LoginInHandler(BaseHandler):
    '''
    登陆处理
    '''
    def get(self):
        self.finish(LoginIn().entry(self))


class IndexHandler(BaseHandler):
    '''
    线上环境起始页
    '''
    def get(self):
        self.render("index.html")


class TotalTaskHandler(BaseHandler):
    '''
    返回所有的任务包信息
    '''
    def get(self):
        self.finish(TotalTask().entry(self))


class AddTaskHandler(BaseHandler):
    '''
    增加任务包
    '''
    def post(self):
        self.finish(AddTask().entry(self))


class DivideTaskHandler(BaseHandler):
    '''
    将任务包划分为子任务
    '''
    def get(self):
        self.finish(ShowTasks().entry(self))

    def post(self):
        self.finish(DivideTask().entry(self))


class PersonIndexHandler(BaseHandler):
    '''
    个人信息页
    '''
    def get(self):
        self.finish(PersonIndex().entry(self))


class MemberManageHandler(BaseHandler):

    def get(self):
        self.finish(MemberManage().entry(self))


class TaskManageHandler(BaseHandler):
    '''
    指定任务的任务详细信息
    '''
    def get(self):
        self.finish(TaskManage().entry(self))


class AllPeopleHandler(BaseHandler):
    '''
    所有人员信息汇总
    '''
    def get(self):
        self.finish(AllPeople().entry(self))


class AddPersonHandler(BaseHandler):
    '''
    增加一个新成员
    '''
    def post(self):
        self.finish(AddPerson().entry(self))


class DeletePersonHandler(BaseHandler):
    '''
    删除一个成员
    '''
    def post(self):
        self.finish(DeletePerson().entry(self))


class ResetPasswordHandler(BaseHandler):
    '''
    成员修改密码
    '''
    def post(self):
        self.finish(ResetPassword().entry(self))


class GetMemberHandler(BaseHandler):
    """
    获取成员列表
    """
    def get(self):
        self.finish(GetMember().entry(self))