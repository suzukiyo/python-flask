from flask import Flask
from presentation.controller.member_controller import MemberController
from presentation.controller.member_controller_api import MemberApiController

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config["JSON_SORT_KEYS"] = False


@app.route('/members')
def member_list():
    return MemberController.list()


@app.route('/members/<member_id>')
def member_detail(member_id):
    return MemberController.detail(member_id)


@app.route('/members', methods=['POST'])
def member_register(member):
    return MemberController.register(member)


@app.route('/api/members')
def member_api():
    return MemberApiController.api()


if __name__ == "__main__":
    app.run(debug=True)
