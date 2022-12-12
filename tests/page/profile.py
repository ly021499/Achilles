# @Time   : 2022/11/17 18:29
# @Author : LOUIE
# @Desc   : 个人信息
from utils import log
from tests.position import camera_pos, profile_pos
from tests.lib.page import Page
from core import air
from utils import factory


class ProfilePage(Page):

    @log.wrap('打开头像')
    def open_avatar_menu(self):
        return self.click(camera_pos.avatar_pos)

    @log.wrap('点击头像一栏')
    def avatar_item(self):
        return self.click(profile_pos.avatar_item_pos)

    @log.wrap('点击头像框一栏')
    def avatar_frame_item(self):
        return self.click(profile_pos.avatar_frame_item_pos)

    @log.wrap('点击名片一栏')
    def business_card_item(self):
        return self.click(profile_pos.business_card_item_pos)

    @log.wrap('随机选择头像')
    def choose_avatar(self):
        return self.click(profile_pos.choose_avatar_pos)

    @log.wrap('点击使用按钮')
    def apply_btn(self):
        return self.click(profile_pos.apply_btn_pos)

    @log.wrap('点击关闭按钮')
    def close_btn(self):
        return self.click(profile_pos.close_btn_pos)

    @log.wrap('修改昵称按钮')
    def rename(self):
        return self.click(profile_pos.rename_btn_pos)

    @log.wrap('编辑签名按钮')
    def edit_signature(self):
        return self.click(profile_pos.edit_signature_btn_pos)

    @log.wrap('编辑头像按钮')
    def edit_avatar(self):
        return self.click(profile_pos.edit_avatar_btn_pos)

    @log.wrap('输入新的昵称')
    def input_nickname(self):
        self.click(profile_pos.inputField_pos)
        air.text(factory.random_name())

    @log.wrap('输入新的签名')
    def input_signature(self):
        self.click(profile_pos.inputField_pos)
        air.text(factory.random_paragraph())

    def get_prompt_text(self):
        text = self.get_text(profile_pos.prompt_text_pos)
        log.info(f'📣 📣 📣 operation: 获取提示文本: {text}')
        return text

    @log.wrap('确认按钮')
    def confirm(self):
        return self.click(profile_pos.confirm_btn_pos)







