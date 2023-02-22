import os

item_dir = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# 根路径路径
_dir = os.path.split(os.path.split(os.path.split(os.path.realpath(__file__))[0])[0])[0]
# 测试文件
case_dir = _dir + r'\case'
# 测试报告路径:
report_dir = _dir + r'\repos'
report_html = report_dir + r'Into_an_interface.html'
# 配置文件路径
Basfig_path = item_dir + r'\config\BasicConfigUration.ini'
