# @Time   : 2022/11/4 16:08
# @Author : LOUIE
# @Desc   : to do something ...
from utils import logwrap
from case.position import music_pos
import re
from case.lib.driver.android_app import get_android_poco_instance


class MusicPage:

    def __init__(self, poco_instance):
        self.poco = get_android_poco_instance()

    def _regex(self, pos):
        recompile = re.compile(r'(?<=\[)\d+?(?=\])')
        s = recompile.search(pos)
        if s:
            index = s.group()
            rep_pos = pos.replace(f"[{index}]", "")
            return rep_pos, int(index)
        return pos, 0

    def _parser_pos(self, pos):
        identifier = '&'
        if identifier not in pos:
            if re.search(r'(?<=\[)\d+?(?=\])', pos):
                rep_pos, index = self._regex(pos)
                print(rep_pos, index)
                return self.poco(rep_pos)[index]
            return self.poco(pos)

        value_list = pos.split(identifier)
        pos_list = []
        for value in value_list:
            pos_list.append(self._regex(value))
        p0, n0 = pos_list[0]
        p1, n1 = pos_list[1]
        return self.poco(p0)[n0].offspring(p1)[n1]

    @logwrap('operation: 打开每日推荐')
    def daily_menu(self):
        self._parser_pos(music_pos.daily_menu_pos).click()
        # self.poco(music_pos.daily_menu_pos)[0].click()

    @logwrap('operation: 点击返回')
    def click_daily_back(self):
        self.poco(music_pos.daily_back_btn_pos).click()

    @logwrap('operation: 点击播放全部')
    def click_play_all_btn(self):
        self.poco(music_pos.play_all_btn_pos).click()

    @logwrap('operation: 打开私人FM')
    def private_fm_menu(self):
        self.poco(text=music_pos.private_fm_menu_pos)[1].click()

    @logwrap('operation: 打开歌单')
    def private_fm_song_sheet(self):
        self.poco(text=music_pos.song_sheet_menu_pos).click()

    @logwrap('operation: 打开排行榜')
    def ranking_list_menu(self):
        self.poco(text=music_pos.ranking_list_menu_pos).click()

    @logwrap('operation: 点击飙升榜单')
    def click_soaring_list(self):
        self.poco(text=music_pos.soaring_list_pos).click()

    @logwrap('operation: 点击更多按钮')
    def click_more_btn(self):
        self.poco.sleep(2)
        self.poco(music_pos.list_item_pos)[0].child(music_pos.more_btn_pos).click()

    @logwrap('operation: 收藏到歌单')
    def click_collect_btn(self):
        self.poco(text=music_pos.collect_btn_pos).click()

    @logwrap('operation: 添加至我喜欢的音乐')
    def add_my_favorite(self):
        self.poco(music_pos.my_favorite_pos).click()

    def transaction(self):
        self.daily_menu()
        # self.click_play_all_btn()
        # self.click_daily_back()
        # self.click_daily_back()

    def transaction2(self):
        self.ranking_list_menu()
        self.click_soaring_list()
        self.click_more_btn()
        self.click_collect_btn()
        self.add_my_favorite()


if __name__ == '__main__':
    MusicPage(1).transaction()








