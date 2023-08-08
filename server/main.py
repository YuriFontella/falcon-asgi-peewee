import falcon.asgi

from src.middlewares.auth import Auth
from src.middlewares.pool import Pool

from errors.storage import StorageError

from src.controllers.suffix import SuffixResource
from src.controllers.users import UsersResource

app = falcon.asgi.App(middleware=[Pool(), Auth()])

suffix = SuffixResource()
user = UsersResource()

app.add_route('/all', suffix, suffix='all')
app.add_route('/list', suffix, suffix='list')

app.add_route('/users', user)
app.add_route('/users/{id}', user, suffix='user')

app.add_error_handler(Exception, StorageError.handle)
