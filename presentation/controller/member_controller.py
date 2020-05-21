from flask import render_template, request
from service.member_service import MemberService
from domain.member.member import Member


class MemberController(object):
    def list(self=None):
        members = MemberService.findList()
        return render_template('member.html', title='list test', members=members)

    def detail(member_id=None):
        if member_id == 'None':
            return render_template('member_detail.html', title='detail test', member=Member.ofEmpty())
        member = MemberService.findDetail(member_id)
        return render_template('member_detail.html', title='detail test', member=member)

    def register(member=None):
        if member == 'None':
            return render_template('member_detail.html', title='detail test', member=Member.ofEmpty())
        member = request.form['member']
        return render_template('member_detail.html', title='register test', member=member)
