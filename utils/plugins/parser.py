# @Time   : 2022/11/2 21:05
# @Author : LOUIE
# @Desc   : 解析excel数据

import re
import time
from openpyxl import load_workbook
import os
import setting


target_drop_bag_path = os.path.join(setting.RES_DIR, 'excel/mapping.xlsx')
drop_bag_path = 'D:\MainTrunk\Excels\Dev\CfgDropBag.xlsx'
equipment_path = 'D:\MainTrunk\Excels\Dev\CfgEquipment.xlsx'
language_path = 'D:\MainTrunk\Excels\Dev\CfgLanguage.xlsx'


def parser_string(string: str):
    """
    正则匹配item的id
    """
    items = re.findall('\{(\d+?)\,', string)
    return items


def get_worksheet_instance(excel_path, sheet_name):
    """
    获得EXCEL表中的sheet操作对象
    """
    workbook = load_workbook(excel_path, data_only=True)
    worksheet = workbook[sheet_name]
    return worksheet, workbook


def get_drop_item():
    """
    获取 CfgDropBag 工作簿中的 掉落母表 中的 drop_item_id 和 drop_item数据
    """
    ws, wb = get_worksheet_instance(drop_bag_path, '掉落母表')
    ws_rows_max = ws.max_row
    idx = 2
    drop_item = {}
    while idx <= ws_rows_max:
        drop_item_name = ws.cell(row=idx, column=2).value
        drop_item = ws.cell(row=idx, column=7).value

        drop_item.update({drop_item_name: parser_string(drop_item)})
        idx += 1
    return drop_item


def get_target_regular_drop_item(sheet_name):
    """
    获取 mapping 表中 对应sheet_name 我想要的数据名称
    """
    ws, wb = get_worksheet_instance(target_drop_bag_path, sheet_name)
    ws_rows_max = ws.max_row
    idx = 2
    target_regular_drop_item = {}
    target_first_drop_item = {}

    while idx <= ws_rows_max:
        drop_item_name = ws.cell(row=idx, column=1).value
        regular_drop_item = ws.cell(row=idx, column=5).value
        first_drop_item = ws.cell(row=idx, column=8).value

        target_regular_drop_item.update({drop_item_name: parser_string(regular_drop_item)})
        target_first_drop_item.update({drop_item_name: parser_string(first_drop_item)})

        idx += 1
    return target_regular_drop_item, target_first_drop_item


def get_equipment_identifier():
    """
    获取 CfgEquipment 工作簿中的 CfgEquipment 表的 穿戴物ID、穿戴物名称
    """
    ws, wb = get_worksheet_instance(equipment_path, 'CfgEquipment')
    ws_rows_max = ws.max_row
    idx = 4
    data = {}
    while idx <= ws_rows_max:
        item_id = ws.cell(row=idx, column=2).value
        item_identifier = ws.cell(row=idx, column=8).value
        data.update({item_id: item_identifier})
        idx += 1
    return data


def get_item_ch_language():
    """
    获取 CfgLanguage 工作簿中的 CfgLanSystem 表的 序号、中文
    """
    ws, wb = get_worksheet_instance(language_path, 'CfgLanSystem')
    ws_rows_max = ws.max_row
    idx = 4
    data = {}
    while idx <= ws_rows_max:
        item_identifier = ws.cell(row=idx, column=2).value
        item_zh = ws.cell(row=idx, column=5).value
        data.update({item_identifier: item_zh})
        idx += 1
    return data


def get_mapping_drop_items(sheet_name):
    """
    从表中拿到对应的名称，再到 CfgDropBag.xlsx - 掉落母表 ，获取名称映射到的 DropItem
    """
    target_regular_drop_items, target_first_drop_items = get_target_regular_drop_item(sheet_name)
    drop_items = get_drop_item()

    start_time = time.time()
    # 第一步：拿到我需要的数据表
    regular_mapping_drop_items = {}
    for level_name, target_drop_items in target_regular_drop_items.items():
        for target_drop_item_id in target_drop_items:
            for k, equ_id in drop_items.items():
                if str(target_drop_item_id) == str(k):
                    regular_mapping_drop_items.update({level_name: equ_id})

    first_mapping_drop_items = {}
    for level_name, target_drop_items in target_first_drop_items.items():
        for target_drop_item_id in target_drop_items:
            for k, equ_id in drop_items.items():
                if str(target_drop_item_id) == str(k):
                    first_mapping_drop_items.update({level_name: equ_id})

    end_time = time.time()
    duration = round(end_time - start_time, 2)
    print(f'duration : {duration} s')

    return regular_mapping_drop_items, first_mapping_drop_items


def get_mapping_equipment_ident(mapping_drop_items):
    equipment_identifier = get_equipment_identifier()
    equipment_ident_dict = {}
    for level_name, equ_ids in mapping_drop_items.items():
        identifier_list = []
        for equ_id in equ_ids:
            for equipment_id, identifier in equipment_identifier.items():
                if str(equipment_id) == str(equ_id):
                    identifier_list.append(identifier)

        equipment_ident_dict.update({level_name: identifier_list})
    return equipment_ident_dict


def get_mapping_ch_name(equipment_ident_dict):
    equipment_ch_name = get_item_ch_language()

    ch_name_dict = {}
    for level_name, identifiers in equipment_ident_dict.items():
        ch_name_list = []
        for identifier in identifiers:
            for ident, ch_name in equipment_ch_name.items():
                if str(ident) == str(identifier):
                    ch_name_list.append(ch_name)

        ch_name_dict.update({level_name: ch_name_list})
    return ch_name_dict


def write_to_excel(sheet_name):
    """
    将数据写入excel
    """
    target_regular_drop_items, target_first_drop_items = get_mapping_drop_items(sheet_name)

    regular_equipment_ident_dict = get_mapping_equipment_ident(target_regular_drop_items)
    regular_ch_name_dict = get_mapping_ch_name(regular_equipment_ident_dict)

    first_equipment_ident_dict = get_mapping_equipment_ident(target_regular_drop_items)
    first_ch_name_dict = get_mapping_ch_name(first_equipment_ident_dict)

    regular_items_data_list = [i for i in regular_ch_name_dict.values()]
    first_items_data_list = [i for i in first_ch_name_dict.values()]

    ws, wb = get_worksheet_instance(target_drop_bag_path, sheet_name)
    ws_rows_max = ws.max_row
    idx = 2

    while idx <= ws_rows_max:
        ws.cell(row=idx, column=8).value = str(regular_items_data_list[idx-2])
        ws.cell(row=idx, column=8).value = str(first_items_data_list[idx-2])
        idx += 1

    wb.save(target_drop_bag_path)


def get_reward_config(sheet_name: str):
    """
    读取奖励的配置数据
    """
    ws, wb = get_worksheet_instance(target_drop_bag_path, sheet_name)
    ws_rows_max = ws.max_row
    idx = 2

    reward_dict = {}
    while idx <= ws_rows_max:
        level_name = ws.cell(row=idx, column=7).value
        reward_list = ws.cell(row=idx, column=8).value
        reward_dict.update({level_name: reward_list})

        idx += 1

    return reward_dict


def get_target_reward_data(reward_dict: dict, level_name: str):

    for level, reward_list in reward_dict.items():
        if level == level_name:
            return eval(reward_list)
    return []


# 分成三个步骤：1.初始化表数据，写入表数据后，存储 2.启动程序后，直接读取表中数据存储为生成器或者字典映射对象 3.每次要拿数据再去生成器中去取就可以了。


def init_reward_data():
    """
    初始化mapping表中的奖励数据
    """
    write_to_excel('元素峡谷')
    write_to_excel('贪婪禁地')
    write_to_excel('茫然遗迹')
    write_to_excel('苍穹之城')
    write_to_excel('虚影殿堂')


def struct_reward_data():
    """
    存储数据为对象
    """
    pass


def get_reward_data():
    """
    获取指定数据对象
    """
    pass


items = get_reward_config('茫然遗迹')
print(get_target_reward_data(items, '戈乌拉1'))
# print(type(get_target_level_reward_list(items, '比娜1')))



