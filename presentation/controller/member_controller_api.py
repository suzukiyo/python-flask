from flask import jsonify
from service.member_service import MemberService


class MemberApiController(object):
    def api(self=None):
        return jsonify({
            'status': 'OK',
            'members': MemberService.findList()
        })
