class Member(object):
    name = ''
    email = ''

    def ofEmpty(self):
        member = ''
        member.name = ''
        member.email = ''
        return Member(member)