import configparser
import os


class red_(object):
    # 初始化库
    def __init__(self, filename_, encoding='utf-8'):
        self.filename_ = filename_
        self.encoding_ = encoding
        self.conf_ = configparser.ConfigParser()

        if os.path.exists(filename_):
            try:
                self.red_conf = self.conf_.read(self.filename_, encoding=encoding)
            except Exception as e:
                raise print("加载配置文件出错：%s" % e)
        else:
            pass

    # 写入
    def write_data(self, section, option, value):
        section_list = self.conf_.sections()
        if section not in section_list:
            self.conf_.add_section(section)
            self.conf_.set(section, option, value)
        else:
            self.conf_.set(section, option, value)

        try:
            with open(self.filename_, "w+") as f:
                self.conf_.write(f)
        except FileNotFoundError as e:
            print("写入配置文件错误: %s" % e)
            raise e

    # 读取
    def red_get(self, section, option):

        return self.conf_.get(section, option)

    def red_int(self, section, option):

        return self.conf_.getint(section, option)

    def red_boolean(self, section, option):

        return self.conf_.getboolean(section, option)


# if __name__ == '__main__':
#     pass
    # path = r"D:\test01\config\BasicConfigUration.ini"
    # t = red_(r"D:\test01\config\BasicConfigUration.ini", "utf-8").red_get('loans_app', 'url')
    # print(t)
    #
    # red_(path).write_data('host_ip', 'url_215', 'http://192.168.122.215:9010')
    # red_(path).write_data('token', 'url_233', 'http://192.168.122.233:9010')
    # t = red_(Basfig_path).red_get('headers', 'login_header')
    # print(t)
