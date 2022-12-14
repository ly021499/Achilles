# @Time   : 2022/11/22 17:22
# @Author : LOUIE
# @Desc   : to do something ...


# 塔尔魔术工坊
class Magic:
    magic_workshop_pos = 'textMatches=塔尔魔术工坊'


# 苍穹之城：已通关
class Sky:
    sky_city_pos = 'textMatches=苍穹之城'
    clear_the_level = '已通关'
    battle_btn_pos = 'BattleBtn'
    sky_level_pos = '100'
    sky_energy_pos = 5


# 元素峡谷：关卡等级、能量消耗、冰元素、火元素、风元素、土元素
class Element:
    element_valley_pos = 'textMatches=元素峡谷'
    element_level_pos = '20'
    element_energy_pos = 15
    ice_element_pos = 'textMatches=冰元素'
    fire_element_pos = 'textMatches=火元素'
    wind_element_pos = 'textMatches=风元素'
    soil_element_pos = 'textMatches=土元素'


class Forbid:
    # 贪婪禁地：研究所关卡等级、能量消耗、药水研究所、黄金谷、黄金谷关卡等级、金钥消耗、黄金谷金钥匙
    forbidden_sector_pos = 'textMatches=贪婪禁地'
    potion_pos = 'textMatches=药水研炼所'
    potion_level_pos = '18'
    potion_energy_pos = 10
    gold_pos = 'textMatches=黄金谷'
    gold_level_pos = '8'
    gold_energy_pos = 1
    golden_key_count_pos = 'nameMatches=TextLabel43'


class Shadow:
    # 虚影殿堂：关卡等级、能量消耗、捍卫者试炼、增援者试炼、射手试炼、法师试炼、刺客试炼、战士试炼
    shadow_keep_pos = 'textMatches=虚影殿堂'
    shadow_level_pos = '8'
    shadow_energy_pos = 10
    first_instance_pos = 'TextLabel0'
    second_instance_pos = 'TextLabel0[1]'
    fighter_pos = 'textMatches=战士试炼'
    defender_pos = 'textMatches=捍卫者试炼'
    marksman_pos = 'textMatches=射手试炼'
    support_pos = 'textMatches=增援者试炼'
    mage_pos = 'textMatches=法师试炼'
    assassin_pos = 'textMatches=刺客试炼'


class Lost:
    # 茫然遗迹：关卡等级、能量消耗、比那、切斯特、戈乌拉、巴比艾尔
    lost_sector_pos = 'textMatches=茫然遗迹'
    lost_level_pos = '20'
    lost_energy_pos = 10
    bihna_pos = 'textMatches=比娜'
    chester_pos = 'textMatches=切斯特'
    guule_pos = 'textMatches=戈乌拉'
    papillaire_pos = 'textMatches=巴比艾尔'


class Public:
    # 公共按钮：返回控件文本、返回上级页面、进入按钮、进入战斗、薇薇安、英雄名称、上场英雄、战斗按钮、点击任意继续、能量值、# 副本关卡名称
    page_title_pos = 'CloseButton>Text'
    close_page_pos = 'Back_02_btn'
    enter_btn_pos = 'textMatches=进入'
    into_battle_pos = 'StartBattleBtn'
    wwa_hero_pos = 'nameMatches=CardContainer[2]'
    hero_name_pos = 'textMatches=薇薇安'
    close_hero_page_pos = 'CloseBtn'
    play_hero_pos = 'Frame_formation_default'
    fighting_pos = 'ButtonStart'
    continue_pos = 'nameMatches=TapClickTip'
    energy_pos = Forbid.golden_key_count_pos
    level_name_pos = 'LevelName'


class Battle:
    is_save_title_pos = 'Desc'
    save_btn_pos = 'OkBtn'


class Reward:
    # 奖励图标、奖励名称、战斗奖励、奖励类型、副本名称、能量
    reward_icon_pos = "itemRoot(Clone)"
    reward_name_pos = 'TextName'
    lost_reward_name_pos = 'Name'
    battle_reward_pos = "ItemComponentMedium_"
    reward_type_pos = "LabelText"
    data_btn_pos = 'DataBtn'
    power_pos = 'Power'


