import logging
import time
import os

# log_path是存放日志的路径
cur_path = os.path.dirname(os.path.realpath(__file__))
log_path = os.path.join(os.path.dirname(cur_path), 'log')



# 不存在就创建
if not os.path.exists(log_path):
    os.mkdir(log_path)
    if os.path.exists(log_path):
        os.makedirs(log_path + './error_logs')
        os.makedirs(log_path + './logs')
else:
    pass
logs_path = log_path + r'\logs'
err_path = log_path + r'\error_logs'


#封装一个日志

class Log(object):

    def __init__(self):

        # 日志名字
        self.logname = os.path.join(logs_path, '%s.logmethod' % time.strftime('%Y_%m_%d'))
        self.errorName = os.path.join(err_path, '%s.logmethod' % time.strftime('%Y_%m_%d'))

        self.logmethod = logging.getLogger()
        self.logmethod.setLevel(logging.DEBUG)
        # 格式
        self.formatter = logging.Formatter('[%(asctime)s] - %(filename)s] - %(levelname)s: %(message)s')

    def __console(self, level, message):

        # 输出到指定logs
        fh = logging.FileHandler(self.logname, 'a', encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logmethod.addHandler(fh)

        # 专门用来输出error信息
        er = logging.FileHandler(self.errorName, 'a', encoding='utf-8')
        er.setLevel(logging.ERROR)
        er.setFormatter(self.formatter)
        self.logmethod.addHandler(er)

        # 输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logmethod.addHandler(ch)

        # 区分日志级别
        if level == 'info':
            self.logmethod.info(message)
        elif level == 'debug':
            self.logmethod.debug(message)
        elif level == 'warning':
            self.logmethod.warning(message)
        elif level == 'error':
            self.logmethod.error(message)

        # 避免日志输出重复问题
        self.logmethod.removeHandler(ch)
        self.logmethod.removeHandler(fh)
        fh.close()

    def debug(self, message):

        self.__console('debug', message)

    def info(self, message):

        self.__console('info', message)

    def warning(self, message):

        self.__console('warning', message)

    def error(self, message):

        self.__console('error', message)


if __name__ == "__main__":
    print(Log().debug("这是测试日志"))
