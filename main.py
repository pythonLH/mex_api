import unittest
import HTMLTestRunnerNew
from common.ptah_object._path import case_dir, report_html

'''加载用例方式：
1、unittest.main()直接加载用例并执行
一般用于脚本调试阶段
2、实例化unittest.TestSuite()一个suite集合，用addTest()方法加载用例
一般用于用例数量很少得自动化场景
suite = unittest.TestSuite()
suite.addTest(Test(“test01”)) //Test代表用例得类名，test01代表Test类下得第一条用例得名称
3、实例化unittest.TestSuite()一个suite集合，用addTests()方法加载多个用例
适用于同一个类下执行多个用例
case_list = [Test(“test01”),Test(‘test01’)]
suite = unittest.TestSuite()
suite.addTests(case_list)
4、用例加载器，TestLoader(),实例化suite集合和加载器loader
suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(Test))
适用于加载一个类执行测试用例方式
5、discover批量加载测试用例
suite = unittest.defaultTestLoader.disciver(用例路径，pattern=“正则匹配用例文件”)'''

discover = unittest.defaultTestLoader.discover(case_dir, pattern="test_*.py", top_level_dir=None)
with open(report_html, 'wb') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, title='进件接口报告')
    runner.run(discover)  # 执行查找到的用例)
