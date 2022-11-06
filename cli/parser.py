import argparse
from loguru import logger

def runner_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-V', '--version', dest='version', action='store_true',
        help="show version")
    parser.add_argument(
        'testcase_paths', nargs='*',
        help="testcase file path")
    parser.add_argument(
        '--no-html-report', action='store_true', default=False,
        help="do not generate html report.")
    parser.add_argument(
        '--html-report-name',
        help="specify html report name, only effective when generating html report.")
    parser.add_argument(
        '--html-report-template',
        help="specify html report template path.")
    parser.add_argument(
        '--log-level', default='INFO',
        help="Specify logging level, default is INFO.")
    parser.add_argument(
        '--log-file',
        help="Write logs to specified file path.")
    parser.add_argument(
        '--dot-env-path',
        help="Specify .env file path, which is useful for keeping sensitive data.")
    parser.add_argument(
        '--failfast', action='store_true', default=False,
        help="Stop the test run on the first error or failure.")
    parser.add_argument(
        '--startproject',
        help="Specify new project name.")
    parser.add_argument(
        '--validate', nargs='*',
        help="Validate JSON testcase format.")
    parser.add_argument(
        '--prettify', nargs='*',
        help="Prettify JSON testcase format.")

    args = parser.parse_args()
    if args.version:
        logger.info('1,0')
        exit(0)


if __name__ == '__main__':
    runner_parser()