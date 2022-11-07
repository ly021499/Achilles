# @Time   : 2022/11/4 16:08
# @Author : LOUIE
# @Desc   : to do something ...


class HomePosition:
    daily_menu_pos = 'text="每日推荐"'
    private_fm_menu_pos = 'text="私人FM"'
    song_sheet_menu_pos = 'text="歌单"'
    ranking_list_menu_pos = 'text="排行榜"'
    audio_book_menu_pos = 'text="有声书"'


class HomePage:

    def __init__(self, poco_instance):
        self.poco = poco_instance

    def daily_menu(self):
        self.poco(HomePosition.daily_menu_pos).click()

    def private_fm_menu(self):
        self.poco(HomePosition.private_fm_menu_pos).click()

    def private_fm_song_sheet(self):
        self.poco(HomePosition.song_sheet_menu_pos).click()

    def ranking_list_menu(self):
        self.poco(HomePosition.ranking_list_menu_pos).click()

    def transaction(self):
        pass








