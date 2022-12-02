# @Time   : 2022/11/8 17:31
# @Author : LOUIE
# @Desc   : to do something ...

from utils.logger import log
import setting
import os
import pytest
import shutil


def open_allure():
    """
    运行完后，自动打开 allure 报告
    :return:
    """

    # 复制environment.properties文件
    raw_file_path = os.path.join(setting.REPORT_DIR, 'environment.properties')
    new_file_path = os.path.join(setting.REPORT_DIR, 'output/environment.properties')

    shutil.copy(raw_file_path, new_file_path)

    output_dir = os.path.join(setting.REPORT_DIR, 'output')
    summary_dir = os.path.join(setting.REPORT_DIR, 'summary')

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    if not os.path.exists(summary_dir):
        os.mkdir(summary_dir)

    generate_allure_cmd = "allure generate {} -o {} --clean".format(output_dir, summary_dir)
    os.system(generate_allure_cmd)

    open_allure_cmd = "allure open {}".format(summary_dir)
    os.system(open_allure_cmd)


def main(env: str = None):

    output_dir = os.path.join(setting.REPORT_DIR, 'output')
    options = ["--alluredir={}".format(output_dir), "--clean-alluredir", setting.CASE_DIR]
    log.info("options list: {}".format(options))

    log.info(" = " * 8 + " Process started, Running tests  " + " = " * 8)
    pytest.main(options)
    log.info(" = " * 8 + " Process finished, Testing is completed " + " = " * 8)
    open_allure()