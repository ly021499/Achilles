# @Time   : 2022/11/4 16:08
# @Author : LOUIE
# @Desc   : to do something ...
from utils import log, logwrap


class HomePosition:
    daily_menu_pos = 'android.view.ViewGroup'
    daily_back_btn_pos = '转到上一层级'
    play_all_btn_pos = 'com.netease.cloudmusic:id/playAllTextView'
    private_fm_menu_pos = 'text="私人FM"'
    song_sheet_menu_pos = 'text="歌单"'
    ranking_list_menu_pos = 'text="排行榜"'
    audio_book_menu_pos = 'text="有声书"'


class HomePage:

    def __init__(self, poco_instance):
        self.poco = poco_instance

    @logwrap('operation: 打开每日推荐')
    def daily_menu(self):
        self.poco(HomePosition.daily_menu_pos)[0].click()

    @logwrap('operation: 点击返回')
    def click_daily_back(self):
        self.poco(HomePosition.daily_back_btn_pos).click()

    @logwrap('operation: 点击播放全部')
    def click_play_all_btn(self):
        self.poco(HomePosition.play_all_btn_pos).click()

    @logwrap('operation: 打开私人FM')
    def private_fm_menu(self):
        self.poco(HomePosition.daily_menu_pos)[1].click()

    def private_fm_song_sheet(self):
        self.poco(HomePosition.song_sheet_menu_pos).click()

    def ranking_list_menu(self):
        self.poco(HomePosition.ranking_list_menu_pos).click()

    def transaction(self):
        self.daily_menu()
        self.click_play_all_btn()
        self.click_daily_back()
        self.click_daily_back()
        self.private_fm_menu()








