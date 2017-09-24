import tornado.web
from views import LoginInHandler, TotalTaskHandler, AddTaskHandler
from views import AllPeopleHandler, PersonIndexHandler


SETTINGS = {
    "debug": True
}

HANDLERS = [
    (r"/login", LoginInHandler),
    (r"/stu", TotalTaskHandler),
    (r"/NewTask", AddTaskHandler),
    (r"/Stu/MyTask", PersonIndexHandler),
    (r"/AllPeople", AllPeopleHandler),
]

application = tornado.web.Application(
    handlers=HANDLERS,
    **SETTINGS)