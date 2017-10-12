import tornado.web
import tornado.ioloop
from login.login_in import LoginIn
from index.total_task import TotalTask
from index.add_task import AddTask
from index.divide_task import DivideTask
from index.task_manage import TaskManage
from index.member_manage import MemberManage
from index.show_tasks import ShowTasks
from person.person_index import PersonIndex
from person.all_people import AllPeople
from peewee import MySQLDatabase


class BaseHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "x-requested-with")
        self.set_header('Access-Control-Allow-Methods', 'GET,POST')
        self.set_header('Access-Control-Allow-Credentials', True)

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
        self.finish(ShowTasks().entry(self))

    def post(self):
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
