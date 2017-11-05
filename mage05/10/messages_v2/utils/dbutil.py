#encoding: utf-8
import MySQLdb
from MySQLdb.cursors import DictCursor

HOST = '127.0.0.1'
PORT = 3306
DB = 'kk2'
USER = 'root'
PASSWD = '881019'
CHARSET = 'utf8'

def execute_commit(sql, args=None):
    conn = MySQLConnection(host=HOST, port=PORT, \
                            user=USER, password=PASSWD, db=DB)
    conn.execute_commit(sql, args)
    conn.close()


def execute_fetch(sql, args=None, one=False):
    conn = MySQLConnection(host=HOST, port=PORT, \
                            user=USER, password=PASSWD, db=DB)
    _rt = conn.execute_fetch(sql, args, one)
    conn.close()
    return _rt


class MySQLConnection(object):

    def __init__(self, user, password, db, host='127.0.0.1', port=3306):
        self.__user = user
        self.__password = password
        self.__db = db
        self.__host = host
        self.__port = port
        self.__charset = 'utf8'
        self.__conn = None
        self.__cur = None

    def __connect(self):
        if self.__conn is None:
            self.__conn = MySQLdb.connect(host=self.__host, port=self.__port, \
                                            user=self.__user, passwd=self.__password, \
                                            db=self.__db, charset=self.__charset)
        if self.__cur is None:
            self.__cur = self.__conn.cursor(DictCursor)


    def close(self):
        if self.__conn:
            self.__conn.commit()
        if self.__cur:
            self.__cur.close()
        if self.__conn:
            self.__conn.close()

    def execute_commit(self, sql, args=None):
        self.__connect()
        self.__cur.execute(sql, args)

    def execute_fetch(self, sql, args=None, one=False):
        _rt = None
        self.__connect()
        self.__cur.execute(sql, args)
        if one:
            _rt = self.__cur.fetchone()
        else:
            _rt = self.__cur.fetchall()

        return _rt
