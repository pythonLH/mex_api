import pymysql
import testcase.Path_
from testcase.redconfig import red_


# 用来查询sql的

class MysqlUtil:

    def __init__(self):
        # 初始化时读取数据库连接配置，没传入database名字
        conf = red_(testcase.Path_.database_dir, encoding='utf-8')
        host = conf.red_get('db_mysql', 'host')
        port = conf.red_int('db_mysql', 'port')
        user = conf.red_get('db_mysql', 'user')
        password = conf.red_get('db_mysql', 'password')

        try:
            self.mysql = pymysql.connect(host=host,
                                         user=user,
                                         password=password,
                                         port=port,
                                         cursorclass=pymysql.cursors.DictCursor)

        except Exception as e:
            print("数据库连接错误:{}".format(e))
            raise e

    def fetch_one(self, sql_):
        cursor = self.mysql.cursor()
        cursor.execute(sql_)
        return cursor.fetchone()

    def fetch_all(self, sql_):
        cursor = self.mysql.cursor()
        cursor.execute(sql_)
        return cursor.fetchall()

    def commit(self):
        self.mysql.commit()

    def close(self):
        self.mysql.close()


if __name__ == '__main__':
    pass
    # sql = "SELECT * FROM `hc_app_per`.`app_user` WHERE `phone` LIKE '%466464664%' LIMIT 0,1000;"
    # print(MysqlUtil().fetch_one(sql))
