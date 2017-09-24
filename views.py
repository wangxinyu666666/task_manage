import tornado.web
import tornado.ioloop
from login.login_in import LoginIn
from index.total_task import TotalTask
from index.add_task import AddTask
from index.divide_task import DivideTask
from index.task_manage import TaskManage
from index.member_manage import MemberManage
from person.person_index import PersonIndex
from person.all_people import AllPeople


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        # self.set_header("Access-Control-Allow-Origin", "*")
        # self.set_header("Access-Control-Max-Age", 3628800)
        # self.set_header('Content-type', 'multipart/form-data')
        # self.set_header("Access-Control-Allow-Headers", "x-requested-with,authorization")
        # self.set_header('Access-Control-Allow-Methods', 'POST,GET,PUT,DELETE,OPTIONS')
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET,POST')
        self.set_header('Access-Control-Allow-Credentials', True)


class LoginInHandler(BaseHandler):

    def get(self):
        self.finish(LoginIn().entry(self))


class TotalTaskHandler(BaseHandler):

    def get(self):
        self.finish(TotalTask().entry(self))


class AddTaskHandler(BaseHandler):

    def post(self):
        self.finish(AddTask().entry(self))


class DivideTaskHandler(BaseHandler):
    
    def get(self):
        self.finish(DivideTask().entry(self))


class PersonIndexHandler(BaseHandler):

    def get(self):
        self.finish(PersonIndex().entry(self))


class MemberManageHandler(BaseHandler):

    def get(self):
        self.finish(MemberManage().entry(self))


class TaskManageHandler(BaseHandler):

    def get(self):
        self.finish(TaskManage().entry(self))


class AllPeopleHandler(BaseHandler):

    def get(self):
        self.finish(AllPeople().entry(self))
