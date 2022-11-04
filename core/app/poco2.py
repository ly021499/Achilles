from poco import Poco
from poco.exceptions import InvalidOperationException
from utils import log

import time


class Poco2:

    def __init__(self, agent, **options):
        self.poco = Poco(agent, **options)

    def click(self, pos):
        try:
            return self.poco.click(pos)
        except InvalidOperationException:
            try:
                for i in range(3):
                    self.sleep(1)
                    return self.poco.click(pos)
            except InvalidOperationException:
                raise InvalidOperationException('Click position out of screen. pos={}'.format(repr(pos)))
            except Exception as e:
                raise e

    def wait_for_any(self, objects, timeout=120):
        return self.poco.wait_for_any(objects, timeout)

    def wait_for_all(self, objects, timeout=120):
        return self.poco.wait_for_all(objects, timeout)

    def swipe(self, p1, p2=None, direction=None, duration=2.0):
        try:
            return self.poco.swipe(p1, p2, direction, duration)
        except Exception as e:
            log.error(f'Swipe origin out of screen. {repr(p1)}')
            raise e

    def long_click(self, pos, duration=2.0):
        try:
            self.poco.long_click(pos=pos, duration=duration)
        except InvalidOperationException:
            try:
                # 重试两次
                for i in range(2):
                    return self.poco.long_click(pos=pos, duration=duration)
            except InvalidOperationException:
                raise InvalidOperationException('Click position out of screen. pos={}'.format(repr(pos)))
            except Exception as e:
                raise e

    def scroll(self, direction='vertical', percent=0.6, duration=2.0):
        return self.poco.scroll(direction, percent, duration)

    def pinch(self, direction='in', percent=0.6, duration=2.0, dead_zone=0.1):
        return self.poco.pinch(direction, percent, duration, dead_zone)

    def snapshot(self, width=720):
        return self.poco.snapshot(width=width)

    def get_screen_size(self):
        return self.poco.get_screen_size()

    def sleep(self, sec):
        log.info(f"sleep {sec} second .")
        time.sleep(sec)


