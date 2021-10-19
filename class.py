from flask import Flask
from flask import render_template
from flask.typing import ResponseReturnValue
from flask.views import View, MethodView

application = Flask(__name__, static_folder='static', template_folder='templates')


class UserList(View):
    methods = ['GET', 'POST']
    decorators = [user_required]

    def dispatch_request(self) -> ResponseReturnValue:
        users = []
        return render_template('users.html', users=users)


class UserView(MethodView):
    def get(self, user_id):
        if not user_id:
            return 'all'
        else:
            return user_id

    def post(self):
        return 'post'

    def put(self, user_id):
        return 'put' + user_id

    def delete(self, user_id):
        return 'delete' + user_id


application.add_url_rule('/users', view_func=UserList.as_view('user_list'))
user_view = UserView.as_view('users')
application.add_url_rule('/users', defaults={'user_id': None}, view_func=user_view, methods=["GET"])
application.add_url_rule('/users', view_func=user_view, methods=['POST'])
application.add_url_rule('/users/<int:user_id>', view_func=user_view, methods=['GET', 'PUT', 'DELETE'])


if __name__ == '__main__':
    application.run()
