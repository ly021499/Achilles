# @Time   : 2022/11/4 16:08
# @Author : LOUIE
# @Desc   : to do something ...
from utils import logwrap


class HomePos:
    daily_menu_pos = 'android.view.ViewGroup'
    daily_back_btn_pos = '转到上一层级'
    play_all_btn_pos = 'com.netease.cloudmusic:id/playAllTextView'
    private_fm_menu_pos = "私人FM"
    song_sheet_menu_pos = "歌单"
    ranking_list_menu_pos = "排行榜"
    soaring_list_pos = '飙升榜'
    audio_book_menu_pos = 'text="有声书"'
    list_item_pos = "com.netease.cloudmusic:id/musicListItemContainer"
    more_btn_pos = "com.netease.cloudmusic:id/actionBtn"
    collect_btn_pos = "收藏到歌单"
    my_favorite = "com.netease.cloudmusic:id/playListName"


class HomePage:

    def __init__(self, poco_instance):
        self.poco = poco_instance

    @logwrap('operation: 打开每日推荐')
    def daily_menu(self):
        self.poco(HomePos.daily_menu_pos)[0].click()

    @logwrap('operation: 点击返回')
    def click_daily_back(self):
        self.poco(HomePos.daily_back_btn_pos).click()

    @logwrap('operation: 点击播放全部')
    def click_play_all_btn(self):
        self.poco(HomePos.play_all_btn_pos).click()

    @logwrap('operation: 打开私人FM')
    def private_fm_menu(self):
        self.poco(text=HomePos.private_fm_menu_pos)[1].click()

    @logwrap('operation: 打开歌单')
    def private_fm_song_sheet(self):
        self.poco(text=HomePos.song_sheet_menu_pos).click()

    @logwrap('operation: 打开排行榜')
    def ranking_list_menu(self):
        self.poco(text=HomePos.ranking_list_menu_pos).click()

    @logwrap('operation: 点击飙升榜单')
    def click_soaring_list(self):
        self.poco(text=HomePos.soaring_list_pos).click()

    @logwrap('operation: 点击更多按钮')
    def click_more_btn(self):
        self.poco.sleep(2)
        self.poco(HomePos.list_item_pos)[0].child(HomePos.more_btn_pos).click()

    @logwrap('operation: 收藏到歌单')
    def click_collect_btn(self):
        self.poco(text=HomePos.collect_btn_pos).click()

    @logwrap('operation: 添加至我喜欢的音乐')
    def add_my_favorite(self):
        self.poco(HomePos.my_favorite).click()

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











