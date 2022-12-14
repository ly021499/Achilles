from tests.proxy.outer.reward import RewardPage
from tests.position.outer_pos import *
from utils import log


class InstanceProxy:

    def __init__(self, poco_instance):
        self.reward = RewardPage(poco_instance)

    @log.wrap('验证【茫然遗迹-比娜】关卡：通关流程、能量消耗、奖励匹配')
    def verify_brush_instance_of_bihna(self):
        self.reward.common_brush_instance(
            Lost.lost_sector_pos, Lost.lost_level_pos,
            Lost.bihna_pos, Lost.lost_energy_pos
        )

    @log.wrap('验证【茫然遗迹-切斯特】关卡：通关流程、能量消耗、奖励匹配')
    def verify_brush_instance_of_chester(self):
        self.reward.common_brush_instance(
            Lost.lost_sector_pos, Lost.lost_level_pos,
            Lost.chester_pos, Lost.lost_energy_pos
        )

    @log.wrap('验证【茫然遗迹-戈乌拉】关卡：通关流程、能量消耗、奖励匹配')
    def verify_brush_instance_of_guule(self):
        self.reward.common_brush_instance(
            Lost.lost_sector_pos, Lost.lost_level_pos,
            Lost.guule_pos, Lost.lost_energy_pos
        )

    @log.wrap('验证【茫然遗迹-巴比艾尔】关卡：通关流程、能量消耗、奖励匹配')
    def verify_brush_instance_of_papillaire(self):
        self.reward.common_brush_instance(
            Lost.lost_sector_pos, Lost.lost_level_pos,
            Lost.papillaire_pos, Lost.lost_energy_pos
        )

    @log.wrap('验证【元素峡谷-冰元素】关卡：通关流程、能量消耗、奖励匹配')
    def verify_brush_instance_of_ice(self):
        self.reward.common_brush_instance(
            Element.element_valley_pos, Element.element_level_pos,
            Element.ice_element_pos, Element.element_energy_pos
        )

    @log.wrap('验证【元素峡谷-冰元素】关卡：通关流程、能量消耗、奖励匹配')
    def verify_brush_instance_of_fire(self):
        self.reward.common_brush_instance(
            Element.element_valley_pos, Element.element_level_pos,
            Element.fire_element_pos, Element.element_energy_pos
        )

    @log.wrap('验证【元素峡谷-冰元素】关卡：通关流程、能量消耗、奖励匹配')
    def verify_brush_instance_of_wind(self):
        self.reward.common_brush_instance(
            Element.element_valley_pos, Element.element_level_pos,
            Element.wind_element_pos, Element.element_energy_pos
        )

    @log.wrap('验证【元素峡谷-冰元素】关卡：通关流程、能量消耗、奖励匹配')
    def verify_brush_instance_of_soil(self):
        self.reward.common_brush_instance(
            Element.element_valley_pos, Element.element_level_pos,
            Element.soil_element_pos, Element.element_energy_pos
        )

    @log.wrap('验证【虚影殿堂-第一个副本】关卡：通关流程、能量消耗、奖励匹配')
    def verify_brush_instance_of_first(self):
        self.reward.common_brush_instance(
            Shadow.shadow_keep_pos, Shadow.shadow_level_pos,
            Shadow.first_instance_pos, Shadow.shadow_energy_pos
        )

    @log.wrap('验证【虚影殿堂-第二个副本】关卡：通关流程、能量消耗、奖励匹配')
    def verify_brush_instance_of_second(self):
        self.reward.common_brush_instance(
            Shadow.shadow_keep_pos, Shadow.shadow_level_pos,
            Shadow.second_instance_pos, Shadow.shadow_energy_pos
        )

    @log.wrap('验证【贪婪禁地-药水研究所】关卡：通关流程、能量消耗、奖励匹配')
    def verify_brush_instance_of_potion(self):
        self.reward.common_brush_instance(
            Forbid.forbidden_sector_pos, Forbid.potion_level_pos,
            Forbid.potion_pos, Forbid.potion_energy_pos
        )

    @log.wrap('验证【贪婪禁地-黄金谷】关卡：通关流程、能量消耗、奖励匹配')
    def verify_brush_instance_of_gold(self):
        self.reward.common_brush_instance(
            Forbid.forbidden_sector_pos, Forbid.gold_level_pos,
            Forbid.gold_pos, Forbid.gold_energy_pos
        )

    @log.wrap('验证【天空之城】关卡：通关流程、能量消耗、奖励匹配')
    def verify_brush_instance_of_sky(self):
        self.reward.brush_sky_city(31, Sky.sky_level_pos)







