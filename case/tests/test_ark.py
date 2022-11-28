# @Time   : 2022/11/16 16:02
# @Author : LOUIE
# @Desc   : to do something ...
from case.lib.driver.unity_app import Unity3dPocoUnit
from case.page.daily import DailyPage
from utils import logcase


# class TestProfile(Unity3dPocoUnit):
#
#     def setUp(self) -> None:
#         self.daily_page = DailyPage(self.poco)
#
#     @logcase
#     def test_a_receive_daily_rewards(self):
#         self.daily_page.receive_daily_rewards()
#
#     @logcase
#     def test_b_receive_mail_rewards(self):
#         self.daily_page.receive_mail_rewards()
#
#
# if __name__ == '__main__':
#     import unittest
#     unittest.main()
