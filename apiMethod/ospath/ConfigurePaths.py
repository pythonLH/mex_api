import os

# 当前文件路径
# print((os.path.realpath(__file__)))
# print(os.path.dirname(os.path.realpath(__file__)))
# print(os.path.dirname(os.path.realpath(__file__)))
# print(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# print(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))

# 跟目录
_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# method目录
item_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 配置文件
database_dir = os.path.join(item_dir, 'config', 'database.ini')
Basfig_path = os.path.join(item_dir, 'config', 'BasicConfigUration.ini')
print("配置文件的路径:{}".format(database_dir))
print("配置文件的路径:{}".format(Basfig_path))
