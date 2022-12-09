from tests.page.reward import RewardPage
from tests.position import outer_pos
from utils import logwrap


class InstanceHandle:

    def __init__(self, poco_instance):
        self.reward = RewardPage(poco_instance)

    @logwrap()
    def verify_pass_lost_sector(self):
        self.reward.execute_instance(outer_pos.lost_sector_pos,
                                     outer_pos.lost_sector_level_pos,
                                     outer_pos.bihna_pos)

    @logwrap()
    def verify_pass_(self):
        self.reward.execute_instance(outer_pos.lost_sector_pos,
                                     outer_pos.lost_sector_level_pos,
                                     outer_pos.chester_pos)

    @logwrap()
    def verify_pass_(self):
        self.reward.execute_instance(outer_pos.lost_sector_pos,
                                     outer_pos.lost_sector_level_pos,
                                     outer_pos.guule_pos)

    @logwrap('茫然遗迹')
    def verify_pass_(self):
        self.reward.execute_instance(outer_pos.lost_sector_pos,
                                     outer_pos.lost_sector_level_pos,
                                     outer_pos.papillaire_pos)

    @logwrap('元素峡谷')
    def verify_pass_(self):
        self.reward.execute_instance(outer_pos.elemental_valley_pos,
                                     outer_pos.lost_sector_level_pos,
                                     outer_pos.papillaire_pos)

    @logwrap()
    def verify_pass_(self):
        self.reward.execute_instance(outer_pos.elemental_valley_pos,
                                     outer_pos.lost_sector_level_pos,
                                     outer_pos.papillaire_pos)

    @logwrap()
    def verify_pass_(self):
        self.reward.execute_instance(outer_pos.elemental_valley_pos,
                                     outer_pos.lost_sector_level_pos,
                                     outer_pos.papillaire_pos)

    @logwrap('元素峡谷')
    def verify_pass_(self):
        self.reward.execute_instance(outer_pos.elemental_valley_pos,
                                     outer_pos.lost_sector_level_pos,
                                     outer_pos.papillaire_pos)

    @logwrap('虚影殿堂')
    def verify_pass_(self):
        self.reward.execute_instance(outer_pos.the_shadow_keep_pos,
                                     outer_pos.the_shadow_keep_level_pos,
                                     outer_pos.papillaire_pos)

    @logwrap('虚影殿堂')
    def verify_pass_(self):
        self.reward.execute_instance(outer_pos.the_shadow_keep_pos,
                                     outer_pos.the_shadow_keep_level_pos,
                                     outer_pos.papillaire_pos)

    @logwrap('贪婪禁地->药水研究所')
    def verify_pass_(self):
        self.reward.execute_instance(outer_pos.forbidden_sector_pos,
                                     outer_pos.potion_level_pos,
                                     outer_pos.potion_pos)

    @logwrap('贪婪禁地->黄金谷')
    def verify_pass_(self):
        self.reward.execute_instance(outer_pos.forbidden_sector_pos,
                                     outer_pos.the_gold_level_pos,
                                     outer_pos.the_gold_pos)









