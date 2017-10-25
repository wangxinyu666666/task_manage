import tornado.web
from views import LoginInHandler, TotalTaskHandler, AddTaskHandler
from views import AllPeopleHandler, PersonIndexHandler
from views import DivideTaskHandler, IndexHandler
from views import DeletePersonHandler, AddPersonHandler, ResetPasswordHandler
from views import GetMemberHandler
import os


SETTINGS = {
    "debug": True,
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
}

HANDLERS = [
    (r"/", IndexHandler),
    (r"/login", LoginInHandler),
    (r"/api/stu", TotalTaskHandler),
    (r"/api/NewTask", AddTaskHandler),
    (r"/api/Stu/MyTask", PersonIndexHandler),
    (r"/api/AllPeople", AllPeopleHandler),
    (r"/api/managetask", DivideTaskHandler),
    (r"/api/deletePerson", DeletePersonHandler),
    (r"/api/addPerson", AddPersonHandler),
    (r"/api/resetPassword", ResetPasswordHandler),
    (r"/api/getMember", GetMemberHandler)
]

application = tornado.web.Application(
    handlers=HANDLERS,
    **SETTINGS)
