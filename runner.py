# @Time   : 2022/11/09 19:05
# @Author : LOUIE
# @Desc   : 日志工具

from utils import log, wechat
from XTestRunner import HTMLTestRunner
import unittest
import setting
import os
import datetime
import logging
import time


class Runner:

    def __init__(self):
        self.test_loader = unittest.TestLoader()

    def _load_tests(self, case_dir):
        """
        加载测试用例
        :param case_dir: 用例目录
        :return: test_suite
        """
        test_suite = unittest.TestSuite()

        # 收集测试用例，添加进测试套件
        loaded_testcase = self.test_loader.discover(start_dir=case_dir)
        test_suite.addTests(loaded_testcase)
        log.warning(loaded_testcase)

        return test_suite

    def _run_suite(self, test_suite, result_path):
        """
        运行测试套件
        :param test_suite: 测试套件
        :param result_path: 日志、报告存放路径
        :return:
        """

        filename = 'achilles-' + str(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")) + '.html'
        filepath = os.path.join(result_path, filename)
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

        return runner.get_report_attributes(result)

    def run(self, case_dir=None):
        """
        运行驱动器
        :param case_dir: 用例目录
        :return:
        """
        # 设置airtest日志等级，debug会输出很多日志
        logger = logging.getLogger("airtest")
        logger.setLevel(logging.INFO)

        dir_name = "achilles" + str(time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time())))
        result_path = os.path.join(setting.REPORT_DIR, dir_name)
        if not os.path.exists(result_path):
            os.mkdir(result_path)

        case_dir = case_dir or setting.CASE_DIR

        log.info(" = " * 8 + " Program started, Running testcases  " + " = " * 8)

        test_suite = self._load_tests(case_dir)

        # runner = unittest.TextTestRunner()
        # runner.run(test_suite)
        self._run_suite(test_suite, result_path)
        # wechat.send_msg()

        log.info(" = " * 8 + " Program finished, Testing is completed " + " = " * 8)


if __name__ == '__main__':
    Runner().run()
