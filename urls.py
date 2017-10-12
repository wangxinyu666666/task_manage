import tornado.web
from views import LoginInHandler, TotalTaskHandler, AddTaskHandler
from views import AllPeopleHandler, PersonIndexHandler
from views import DivideTaskHandler


SETTINGS = {
    "debug": True
}

HANDLERS = [
    (r"/login", LoginInHandler),
    (r"/stu", TotalTaskHandler),
    (r"/NewTask", AddTaskHandler),
    (r"/Stu/MyTask", PersonIndexHandler),
    (r"/AllPeople", AllPeopleHandler),
    (r"/managetask", DivideTaskHandler),
]

application = tornado.web.Application(
    handlers=HANDLERS,
    **SETTINGS)