# @Time   : 2022/11/08 17:05
# @Author : LOUIE
# @Desc   : 日志工具

from utils import log, wechat
from XTestRunner import HTMLTestRunner
import unittest
import setting
import os
import datetime


class Runner:

    def __init__(self):
        self.test_loader = unittest.TestLoader()

    def _add_tests(self, testcases):
        def _add_step(config, variable, test_dict):
            def test(self):
                try:
                    run_test(config, variable, test_dict)
                except Exception as ex:
                    self.fail(str(ex))
            return test

        test_suite = unittest.TestSuite()

        for testcase in testcases:

            config = testcase.get("config", {})
            case_desc = config.get('case_desc', 'no description')
            export = config.get('export', {})

            teststeps = testcase.get("steps", [])

            # 使用type生成测试用例类
            TestSequense = type(config.get('case_name', 'TestSequense'), (unittest.TestCase,), {})
            # 添加类注释，可以在报告中展示明细
            TestSequense.__doc__ = case_desc

            # 分解成用例类中的用例方法
            for index, tests_dict in enumerate(teststeps):
                test_func_name = 'test_{:04}'.format(index)
                test_func = _add_step(config, variable, tests_dict)
                test_desc = tests_dict.get('name', test_func_name)
                setattr(TestSequense, test_func_name, test_func)
                func = getattr(TestSequense, test_func_name)
                func.__doc__ = test_desc

            # 收集测试用例，添加进测试套件
            loaded_testcase = self.test_loader.loadTestsFromTestCase(TestSequense)
            test_suite.addTest(loaded_testcase)

        return test_suite

    def _run_suite(self, test_suite):
        """
        运行测试套件
        :param test_suite:
        :return:
        """

        filename = str(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")) + '.html'
        filepath = os.path.join(setting.RESULT_DIR, filename)
        with open(filepath, 'wb+') as fp:
            runner = HTMLTestRunner(
                stream=fp,
                title=setting.TITLE,
                description=setting.DESCRIPTION,
                language='zh-CN',
                tester=setting.TESTER
            )
            result = runner.run(
                testlist=test_suite,
                rerun=setting.RERUN,
                save_last_run=False
            )
        log.info(f'Generating HTML reports... filepath: {filepath}')

        # 发送邮件
        # send_email(filepath)

        attr = runner.get_report_attributes(result)
        return attr

    def run(self, *file_or_dir, **kwargs):
        """
        运行程序函数
        :param file_or_dir:
        :param kwargs:
        :return:
        """
        log.info(" = " * 8 + " Program started, Running testcases  " + " = " * 8)
        if "env" in kwargs.keys():
            setting.ENV = kwargs.get("env").lower()
        if file_or_dir:
            file_list = [(os.path.join(setting.CASE_DIR, filename)) for filename in file_or_dir]
        else:
            file_list = loader.load_folder(CASE_DIR)
        testcases = []
        for filepath in file_list:
            test_dict = loader.load_yaml(filepath=filepath)
            testcase_name = test_dict.get("config").get("case_desc")
            log.info("Start to collect testcase: {}".format(testcase_name))
            testcases.append(test_dict)
        test_suite = self._add_tests(testcases=testcases)
        result = self._run_suite(test_suite)
        result = parse_summary(result)
        wechat.send_msg()
        log.info(" = " * 8 + " Program finished, Testing is completed " + " = " * 8)


if __name__ == '__main__':
    Runner().run()
