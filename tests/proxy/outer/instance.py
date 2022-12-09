from tests.page.reward import RewardPage
from tests.position.outer_pos import *
from utils import logwrap


class InstanceProxy:

    def __init__(self, poco_instance):
        self.reward = RewardPage(poco_instance)

    @logwrap('验证【茫然遗迹-比娜】副本所有关卡的能量消耗是否正确及战斗奖励是否与运营配置符合')
    def verify_brush_instance_of_bihna(self):
        self.reward.brush_instance(
            Lost.lost_sector_pos, Lost.lost_level_pos,
            Lost.bihna_pos, Lost.lost_energy_pos
        )

    @logwrap('验证【茫然遗迹-切斯特】副本所有关卡的能量消耗是否正确及战斗奖励是否与运营配置符合')
    def verify_brush_instance_of_chester(self):
        self.reward.brush_instance(
            Lost.lost_sector_pos, Lost.lost_level_pos,
            Lost.chester_pos, Lost.lost_energy_pos
        )

    @logwrap('验证【茫然遗迹-戈乌拉】副本所有关卡的能量消耗是否正确及战斗奖励是否与运营配置符合')
    def verify_brush_instance_of_guule(self):
        self.reward.brush_instance(
            Lost.lost_sector_pos, Lost.lost_level_pos,
            Lost.guule_pos, Lost.lost_energy_pos
        )

    @logwrap('验证【茫然遗迹-巴比艾尔】副本所有关卡的能量消耗是否正确及战斗奖励是否与运营配置符合')
    def verify_brush_instance_of_papillaire(self):
        self.reward.brush_instance(
            Lost.lost_sector_pos, Lost.lost_level_pos,
            Lost.papillaire_pos, Lost.lost_energy_pos
        )

    @logwrap('验证【元素峡谷-冰元素】副本所有关卡的能量消耗是否正确及战斗奖励是否与运营配置符合')
    def verify_brush_instance_of_ice(self):
        self.reward.brush_instance(
            Element.element_valley_pos, Element.element_level_pos,
            Element.ice_element_pos, Element.element_energy_pos
        )

    @logwrap('验证【元素峡谷-冰元素】副本所有关卡的能量消耗是否正确及战斗奖励是否与运营配置符合')
    def verify_brush_instance_of_fire(self):
        self.reward.brush_instance(
            Element.element_valley_pos, Element.element_level_pos,
            Element.fire_element_pos, Element.element_energy_pos
        )

    @logwrap('验证【元素峡谷-冰元素】副本所有关卡的能量消耗是否正确及战斗奖励是否与运营配置符合')
    def verify_brush_instance_of_wind(self):
        self.reward.brush_instance(
            Element.element_valley_pos, Element.element_level_pos,
            Element.wind_element_pos, Element.element_energy_pos
        )

    @logwrap('验证【元素峡谷-冰元素】副本所有关卡的能量消耗是否正确及战斗奖励是否与运营配置符合')
    def verify_brush_instance_of_soil(self):
        self.reward.brush_instance(
            Element.element_valley_pos, Element.element_level_pos,
            Element.soil_element_pos, Element.element_energy_pos
        )

    @logwrap('验证【虚影殿堂-法师试炼】副本所有关卡的能量消耗是否正确及战斗奖励是否与运营配置符合')
    def verify_brush_instance_of_mage(self):
        self.reward.brush_instance(
            Shadow.shadow_keep_pos, Shadow.shadow_keep_level_pos,
            Shadow.mage_pos, Shadow.shadow_energy_pos
        )

    @logwrap('验证【虚影殿堂-增援者试炼】副本所有关卡的能量消耗是否正确及战斗奖励是否与运营配置符合')
    def verify_brush_instance_of_support(self):
        self.reward.brush_instance(
            Shadow.shadow_keep_pos, Shadow.shadow_keep_level_pos,
            Shadow.support_pos, Shadow.shadow_energy_pos
        )

    # @logwrap('验证【虚影殿堂-战士试炼】副本所有关卡的能量消耗是否正确及战斗奖励是否与运营配置符合')
    # def verify_brush_instance_of_support(self):
    #     self.reward.brush_instance(
    #         Shadow.shadow_keep_pos, Shadow.shadow_keep_level_pos,
    #         Shadow.fighter_pos, Shadow.shadow_energy_pos
    #     )

    # @logwrap('验证【虚影殿堂-增援者试炼】副本所有关卡的能量消耗是否正确及战斗奖励是否与运营配置符合')
    # def verify_brush_instance_of_support(self):
    #     self.reward.brush_instance(
    #         Shadow.shadow_keep_pos, Shadow.shadow_keep_level_pos,
    #         Shadow.fighter_pos, Shadow.shadow_energy_pos
    #     )
    #
    # @logwrap('验证【虚影殿堂-增援者试炼】副本所有关卡的能量消耗是否正确及战斗奖励是否与运营配置符合')
    # def verify_brush_instance_of_support(self):
    #     self.reward.brush_instance(
    #         Shadow.shadow_keep_pos, Shadow.shadow_keep_level_pos,
    #         Shadow.fighter_pos, Shadow.shadow_energy_pos
    #     )
    #
    # @logwrap('验证【虚影殿堂-增援者试炼】副本所有关卡的能量消耗是否正确及战斗奖励是否与运营配置符合')
    # def verify_brush_instance_of_support(self):
    #     self.reward.brush_instance(
    #         Shadow.shadow_keep_pos, Shadow.shadow_keep_level_pos,
    #         Shadow.fighter_pos, Shadow.shadow_energy_pos
    #     )
    #
    @logwrap('验证【贪婪禁地-药水研究所】副本所有关卡的能量消耗是否正确及战斗奖励是否与运营配置符合')
    def verify_brush_instance_of_potion(self):
        self.reward.brush_instance(
            Forbid.forbidden_sector_pos, Forbid.potion_level_pos,
            Forbid.potion_pos, Forbid.potion_energy_pos
        )

    @logwrap('验证【贪婪禁地-黄金谷】副本所有关卡的能量消耗是否正确及战斗奖励是否与运营配置符合')
    def verify_brush_instance_of_gold(self):
        self.reward.brush_instance(
            Forbid.forbidden_sector_pos, Forbid.gold_level_pos,
            Forbid.gold_pos, Forbid.gold_energy_pos
        )









