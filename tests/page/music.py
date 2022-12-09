# @Time   : 2022/11/4 16:08
# @Author : LOUIE
# @Desc   : to do something ...
from utils import logwrap
from tests.position import battle_pos
from tests.lib.page import Page


class MusicPage(Page):

    @logwrap('operation: 打开每日推荐')
    def daily_menu(self):
        self.click(music_pos.daily_menu_pos)

    @logwrap('operation: 点击返回上一级')
    def click_daily_back(self):
        self.click(music_pos.daily_back_btn_pos)

    @logwrap('operation: 点击播放全部')
    def click_play_all_btn(self):
        self.click(music_pos.play_all_btn_pos)

    @logwrap('operation: 打开私人FM')
    def private_fm_menu(self):
        self.click(music_pos.private_fm_menu_pos)

    @logwrap('operation: 打开歌单')
    def private_fm_song_sheet(self):
        self.click(music_pos.song_sheet_menu_pos)

    @logwrap('operation: 打开排行榜')
    def ranking_list_menu(self):
        self.click(music_pos.ranking_list_menu_pos)

    @logwrap('operation: 点击飙升榜单')
    def click_soaring_list(self):
        self.click(music_pos.soaring_list_pos)

    @logwrap('operation: 点击更多按钮')
    def click_more_btn(self):
        self.poco.sleep(1)
        self.click(music_pos.list_item_pos)

    @logwrap('operation: 收藏到歌单')
    def click_collect_btn(self):
        self.click(music_pos.collect_btn_pos)

    @logwrap('operation: 添加至我喜欢的音乐')
    def add_my_favorite(self):
        self.click(music_pos.my_favorite_pos)

    def transaction(self):
        self.daily_menu()
        self.click_play_all_btn()
        self.click_daily_back()
        self.click_daily_back()

    def transaction2(self):
        self.ranking_list_menu()
        self.click_soaring_list()
        self.click_more_btn()
        self.click_collect_btn()
        self.add_my_favorite()


if __name__ == '__main__':
    MusicPage(1).transaction()








