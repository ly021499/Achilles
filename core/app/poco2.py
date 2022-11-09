# @Time   : 2022/11/4 14:14
# @Author : LOUIE
# @Desc   : poco核心api的二次封装

from poco import Poco
from poco.exceptions import InvalidOperationException, PocoNoSuchNodeException
from utils import log

import time


class Poco2(Poco):

    def click(self, pos):
        try:
            return super().click(pos)
        except (InvalidOperationException, PocoNoSuchNodeException):
            try:
                # Retry twice
                self.sleep(1)
                return super().click(pos)
            except InvalidOperationException as e:
                log.error(f'Click position out of screen. pos={repr(pos)}')
                raise InvalidOperationException(f'Click position out of screen. pos={repr(pos)}') from e
            except Exception as e:
                log.error(f'Failed to click position, Exc:{e}')
                raise e

    def wait_for_any(self, objects, timeout=120):
        try:
            log.info(f'Wait for any {objects}')
            return super().wait_for_any(objects, timeout)
        except Exception as e:
            log.error(f'Failed to wait for any {objects}')
            raise e

    def wait_for_all(self, objects, timeout=120):
        try:
            log.info(f'Wait for all {objects}, timeout: {timeout}')
            return super().wait_for_all(objects, timeout)
        except Exception as e:
            log.error(f'Failed to wait for all {objects}')
            raise e

    def swipe(self, p1, p2=None, direction=None, duration=2.0):
        try:
            log.info(f'Swipe origin {repr(p1)}, duration: {duration}')
            return super().swipe(p1, p2, direction, duration)
        except Exception as e:
            log.error(f'Swipe origin out of screen. {repr(p1)}')
            raise e

    def long_click(self, pos, duration=2.0):
        try:
            log.info(f'Long click position: {pos}, duration: {duration}')
            return super().long_click(pos=pos, duration=duration)
        except InvalidOperationException:
            try:
                # Retry twice
                for _ in range(2):
                    return super().long_click(pos=pos, duration=duration)
            except InvalidOperationException as e:
                log.error(f'Long click position out of screen. pos={repr(pos)}')
                raise InvalidOperationException(f'Click position out of screen. pos={repr(pos)}') from e
            except Exception as e:
                log.error(f'Failed to long click position, Exc:{e}')
                raise e

    def scroll(self, direction='vertical', percent=0.6, duration=2.0):
        try:
            log.info(f'Scroll to position, direction: {direction}, percent: {percent}, duration: {duration}')
            return super().scroll(direction, percent, duration)
        except Exception as e:
            log.info(f'Failed to scroll position, direction: {direction}, percent: {percent}, duration: {duration}')
            raise e

    def pinch(self, direction='in', percent=0.6, duration=2.0, dead_zone=0.1):
        return super().pinch(direction, percent, duration, dead_zone)

    def snapshot(self, width=720):
        try:
            log.info(f'Save the snapshot, width: {width}')
            return super().snapshot(width=width)
        except Exception as e:
            log.info(f'Failed to save the snapshot, width: {width}')
            raise e

    def get_screen_size(self):
        try:
            screen_size = super().get_screen_size()
            log.info(f'Get screen size: {screen_size}')
            return screen_size
        except Exception as e:
            log.info('Failed to get screen size')
            raise e

    def start_gesture(self, pos):
        try:
            log.info(f'Start gesture, position: {pos}')
            return super().start_gesture(pos)
        except Exception as e:
            log.info(f'Failed to start gesture, position: {pos}')
            raise e

    def apply_motion_tracks(self, tracks, accuracy=0.004):
        try:
            log.info(f'Apply motion tracks: {tracks}, accuracy: {accuracy}')
            return super().apply_motion_tracks(tracks, accuracy)
        except Exception as e:
            log.info(f'Failed to apply motion tracks: {tracks}, accuracy: {accuracy}')
            raise e

    def sleep(self, sec=1.0):
        log.debug(f"sleep {sec} seconds .")
        time.sleep(sec)


