# 解析excel数据
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
    获取 CfgDropBag 工作簿中的 Sheet1 表的 drop_item_id 和 drop_item数据
    """
    ws, wb = get_worksheet_instance(drop_bag_path, '掉落母表')
    ws_rows_max = ws.max_row
    idx = 2
    drop_item = {}
    while idx <= ws_rows_max:
        drop_item_id = ws.cell(row=idx, column=2).value
        drop_item_str = ws.cell(row=idx, column=7).value
        parser_drop_item = parser_string(drop_item_str)
        drop_item.update({drop_item_id: parser_drop_item})
        idx += 1
    return drop_item


def get_target_item(sheet_name):
    """
    获取我想要的数据名称
    """
    ws, wb = get_worksheet_instance(target_drop_bag_path, sheet_name)
    ws_rows_max = ws.max_row
    idx = 2
    target_drop_item = {}
    while idx <= ws_rows_max:
        drop_item_id = ws.cell(row=idx, column=1).value
        drop_item_str = ws.cell(row=idx, column=5).value
        parser_drop_item = parser_string(drop_item_str)
        target_drop_item.update({drop_item_id: parser_drop_item})
        idx += 1
    return target_drop_item


def get_equipment_identifier():
    """
    获取 CfgEquipment 工作簿中的 CfgEquipment 表的 穿戴物ID、穿戴物名称
    """
    ws, wb = get_worksheet_instance(equipment_path, 'CfgEquipment')
    ws_rows_max = ws.max_row
    idx = 4
    data = {}
    while idx <= ws_rows_max:
        drop_item_id = ws.cell(row=idx, column=2).value
        item_identifier = ws.cell(row=idx, column=8).value
        data.update({drop_item_id: item_identifier})
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


def mapping_drop_item(sheet_name):
    """
    从表中拿到对应的名称，再到 CfgDropBag.xlsx - 掉落母表 ，获取名称映射到的 DropItem
    """
    target_items = get_target_item(sheet_name)
    drop_items = get_drop_item()
    equipment_identifier = get_equipment_identifier()
    equipment_ch_name = get_item_ch_language()

    start_time = time.time()
    # 第一步：拿到我需要的数据表
    data = {}
    for level_name, target_drop_items in target_items.items():
        for target_drop_item_id in target_drop_items:
            for k, equ_id in drop_items.items():
                if str(target_drop_item_id) == str(k):
                    data.update({level_name: equ_id})

    data2 = {}
    for level_name, equ_ids in data.items():
        identifier_list = []
        for equ_id in equ_ids:
            for equipment_id, identifier in equipment_identifier.items():
                if str(equipment_id) == str(equ_id):
                    identifier_list.append(identifier)

        data2.update({level_name: identifier_list})

    data3 = {}
    for level_name, identifiers in data2.items():
        ch_name_list = []
        for identifier in identifiers:
            for ident, ch_name in equipment_ch_name.items():
                if str(ident) == str(identifier):
                    ch_name_list.append(ch_name)

        data3.update({level_name: ch_name_list})

    end_time = time.time()
    duration = round(end_time - start_time, 2)
    print(f'duration : {duration} s')

    return data3


def write_to_excel(sheet_name):
    items_data = mapping_drop_item(sheet_name)
    items_data_list = [i for i in items_data.values()]
    ws, wb = get_worksheet_instance(target_drop_bag_path, sheet_name)
    ws_rows_max = ws.max_row
    idx = 2

    while idx <= ws_rows_max:
        ws.cell(row=idx, column=8).value = str(items_data_list[idx-2])
        idx += 1

    wb.save(target_drop_bag_path)


def get_reward_config(sheet_name):
    ws, wb = get_worksheet_instance(target_drop_bag_path, sheet_name)
    ws_rows_max = ws.max_row
    idx = 2

    reward_dict = {}
    while idx <= ws_rows_max:
        level_name = ws.cell(row=idx, column=7).value
        reward_name = ws.cell(row=idx, column=8).value
        reward_dict.update({level_name: reward_name})

        idx += 1

    return reward_dict


def parser_level_name(s: str):
    instance_type, level = s.split('-')
    print(instance_type, level)

# write_to_excel('元素峡谷')
# write_to_excel('贪婪禁地')
# write_to_excel('茫然遗迹')
# write_to_excel('苍穹之城')
# write_to_excel('虚影殿堂')


# print(get_reward_config('茫然遗迹'))

parser_level_name('比娜-1')



