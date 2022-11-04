from utils.logger import log
import setting
import os
import sys
import pytest
import shutil


def add_arguments():
    args = sys.argv[1:][0].split('--')[1].lower()
    arguments = ['test', 'prod', 'fat', 'pre']
    if args not in arguments:
        help_text = """
        prompt: only four environment parameters are supported\n
        :params: --test
        :params: --fat
        :params: --pre
        :params: --prod
        """
        print(help_text)
        log.error(help_text)
        return
    else:
        setting.ENV = args
        print('Current Operating Environment:  {}'.format(setting.ENV))
        log.info(f'Current Operating Environment:{setting.ENV}\n')


def open_allure():
    """
    运行完后，自动打开 allure 报告
    :return:
    """

    # 复制environment.properties文件
    raw_file_path = os.path.join(setting.RESULT_DIR, 'environment.properties')
    new_file_path = os.path.join(setting.RESULT_DIR, 'output/environment.properties')

    shutil.copy(raw_file_path, new_file_path)

    output_dir = os.path.join(setting.RESULT_DIR, 'output')
    summary_dir = os.path.join(setting.RESULT_DIR, 'summary')

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    if not os.path.exists(summary_dir):
        os.mkdir(summary_dir)

    generate_allure_cmd = "allure generate {} -o {} --clean".format(output_dir, summary_dir)
    os.system(generate_allure_cmd)

    open_allure_cmd = "allure open {}".format(summary_dir)
    os.system(open_allure_cmd)


def main(env=None):
    if env:
        add_arguments()
    else:
        if env is None:
            env = 'prod'
        setting.ENV = env

    output_dir = os.path.join(setting.RESULT_DIR, 'output')
    options = ["--alluredir={}".format(output_dir), "--clean-alluredir", setting.CASE_DIR]
    log.info("options list: {}".format(options))

    log.info(" = " * 8 + " Process started, Running tests  " + " = " * 8)
    pytest.main(options)
    log.info(" = " * 8 + " Process finished, Testing is completed " + " = " * 8)
    open_allure()


if __name__ == '__main__':
    main()