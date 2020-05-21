from infrastructure.configuration.database_manager import DatabaseManager


class MemberService(object):
    def findList(self=None):
        sql = "select * from members"
        return DatabaseManager.fetch(sql)

    def findDetail(member_id):
        sql = "select * from members where id = %s" % member_id
        return DatabaseManager.fetch(sql)[0]
