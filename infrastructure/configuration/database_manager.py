import pymysql

class DatabaseManager(object):
    def getConnection(self=None):
        return pymysql.connect(
            host='localhost',
            user='root',
            password='secret',
            db='testdb',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
        )

    def fetch(sql=None):
        db = DatabaseManager.getConnection()
        cur = db.cursor()
        cur.execute(sql)
        result = cur.fetchall()

        cur.close()
        db.close()

        return result