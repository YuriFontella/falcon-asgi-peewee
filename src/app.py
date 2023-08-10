import falcon.asgi

from src.middlewares.auth import Auth
from src.middlewares.pool import Pool

from src.storage.error import StorageError
from src.storage.limits import Limiter

from src.controllers.users import UsersResource

app = falcon.asgi.App(middleware=[Pool(), Auth(), Limiter()])

user = UsersResource()

app.add_route('/users', user)
app.add_route('/users/{id}', user, suffix='user')

app.add_error_handler(Exception, StorageError.handle)
