# @Time   : 2022/11/10 15:17
# @Author : LOUIE
# @Desc   : 每日日常
from utils import logwrap
from case.position import reward_pos
from case.lib.page import Page


# 每日登录、领取奖励、关闭每日任务按钮、打开邮件、一键领取、战报、一键阅读
daily_item_pos = 'Item_Daily'
receive_rewards_pos = "Button_Get"
system_mail_pos = 'texture=Icon_SystemMail'
express_receipt_pos = "Button_AllCollect"
close_task_btn_pos = 'Btn_Close'
war_report_pos = 'Button_2'
read_all_pos = 'Button_ReadAll'


class DailyPage(Page):

    @logwrap('每日登录')
    def daily_item(self):
        self.click(daily_item_pos)

    @logwrap('领取奖励')
    def receive_rewards(self):
        self.click(receive_rewards_pos)

    @logwrap('关闭任务页面')
    def close_task_page(self):
        self.click(close_task_btn_pos)

    @logwrap('打开系统邮件')
    def open_system_mail(self):
        self.click(system_mail_pos)

    @logwrap("一键领取")
    def express_receipt(self):
        self.click(express_receipt_pos)

    @logwrap("点击战报")
    def close_hero_note(self):
        self.click(war_report_pos)

    @logwrap("一键阅读")
    def read_all(self):
        if self.exists(read_all_pos):
            self.click(read_all_pos)

    def receive_daily_rewards(self):
        self.daily_item()
        if self.exists(receive_rewards_pos):
            self.receive_rewards()
        self.close_task_page()

    def receive_mail_rewards(self):
        self.open_system_mail()
        self.express_receipt()
        self.close_hero_note()
        self.read_all()
        self.close_task_page()


if __name__ == '__main__':
    from core.lib.driver.unity_window import get_unity_window_poco_instance
    page = DailyPage(get_unity_window_poco_instance())
    page.receive_daily_rewards()






















