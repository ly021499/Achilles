import argparse
from loguru import logger


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-V', '--version', dest='version', action='store_true', help="show version")
    parser.add_argument(
        'testcase_path', nargs='*', help="testcase file path")
    parser.add_argument(
        '--log-level', default='INFO', help="Specify logging level, default is INFO.")
    parser.add_argument(
        '--not-save-log', default='INFO', help="Specify logging level, default is INFO.")
    parser.add_argument(
        '--failfast', action='store_true', default=False, help="Stop the tests run on the first error or failure.")

    args = parser.parse_args()
    return args


def runner_parser():
    args = get_parser()
    if args.version:
        print('version achilles-1.0')
    if args.testcase_path:
        print('testcase_path')


if __name__ == '__main__':
    runner_parser()
