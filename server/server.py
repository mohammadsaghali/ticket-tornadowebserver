import os.path
import torndb
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
import os
from binascii import hexlify
import tornado.web
from tornado.options import define, options
import time

define("port", default=1104, help="run on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="database host")
define("mysql_database", default="tickets", help="database name")
define("mysql_user", default="x", help="database user")
define("mysql_password", default="y", help="database password")


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/signup", signup),
            (r"/apicheck", apicheck),
            (r"/authcheck", authcheck),
            (r"/logout",logout),
            (r"/sendTicket",sendTicket),
            (r".*", defaulthandler),
        ]
        settings = dict()
        super(Application, self).__init__(handlers, **settings)
        self.db = torndb.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password)


class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db
    def check_user(self,user):
        resuser = self.db.get("SELECT * from users where username = %s",user)
        if resuser:
            return True
        else :
            return False

    def check_api(self,api):
        resuser = self.db.get("SELECT * from users where apitoken = %s", api)
        if resuser:
            return True
        else:
            return False

    def check_auth(self,username,password):
        resuser = self.db.get("SELECT * from users where username = %s and password = %s", username, password)
        if resuser:
            return True
        else:
            return False

class defaulthandler(BaseHandler):
    def get(self):
        user = self.db.get("SELECT * from users where username = 'mohammadsgh'")
        self.write(user)


class signup(BaseHandler):
    def post(self, *args, **kwargs):
        username = self.get_argument('username')
        password = self.get_argument('password')
        role = self.get_argument('role')
        firstname = self.get_argument('firstname')
        lastname = self.get_argument('lastname')
        if not self.check_user(username):
            api_token = str(hexlify(os.urandom(16)))
            user_id = self.db.execute("INSERT INTO users (username, password, role, apitoken, firstname, lastname) "
                                     "values (%s,%s,%s,%s,%s,%s) "
                                     , username,password, role, api_token, firstname, lastname)
            output = {'apitoken' : api_token,
                      'status': 'OK'}
            self.write(output)
        else :
            output = {'status': 'User Exist'}
            self.write(output)

class apicheck(BaseHandler):
    def post(self, *args, **kwargs):
        api = self.get_argument('api')
        if self.check_api(api):
            user = self.db.get("SELECT * from users where apitoken = %s", api)
            output = {'status': 'TRUE',
                      'api': user.apitoken,
                      'username': user.username}
            self.write(output)
        else:
            output = {'status': 'FALSE'}
            self.write(output)


class authcheck(BaseHandler):
    def post(self, *args, **kwargs):
        username = self.get_argument('username')
        password = self.get_argument('password')
        if self.check_auth(username,password):
            user = self.db.get("SELECT * from users where username = %s and password = %s", username, password)
            output = {'status': 'TRUE',
                      'api': user.apitoken,
                      'username': user.username}
            self.write(output)
        else:
            output = {'status': 'FALSE'}
            self.write(output)


class logout(BaseHandler):
    def post(self):
        username = self.get_argument('username')
        password = self.get_argument('password')


class sendTicket(BaseHandler):
    def post(self):
        apiToken = self.get_argument('apiToken')
        subject = self.get_argument('subject')
        body = self.get_argument('body')

        user = self.db.get("SELECT id FROM users WHERE apitoken = %s", apiToken)

        self.db.execute("INSERT INTO ticket (userId, subject, body, response, status, date)"
                            "VALUES (%s,%s,%s,%s,'open', %s)", int(user.id), subject, body, None,
                            time.strftime('%Y-%m-%d %H:%M:%S'))
        ticket_id = self.db.execute("SELECT LAST_INSERT_ID()")
        message = {'message': 'Ticket Sent Successfully!', 'id': ticket_id,'status': 'OK'}
        self.write(message)

def main():
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
