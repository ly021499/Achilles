# @Time   : 2022/11/2 21:05
# @Author : LOUIE
# @Desc   : 解析excel数据

from utils.excel_tool import ExcelTool
import re
import os
import setting


mapping_path = os.path.join(setting.RES_DIR, 'excel\\mapping.xlsx')
drop_bag_path = 'D:\\MainTrunk\\Excels\\Dev\\CfgDropBag.xlsx'
equipment_path = 'D:\\MainTrunk\\Excels\\Dev\\CfgEquipment.xlsx'
language_path = 'D:\\MainTrunk\\Excels\\Dev\\CfgLanguage.xlsx'
item_path = 'D:\\MainTrunk\\Excels\\Dev\\CfgItem.xlsx'
dungeon_path = 'D:\\MainTrunk\\Excels\\Dev\\CfgDungeon.xlsx'


def parser_string(string: str):
    """
    正则匹配item的id
    """
    items = re.findall(r'\{(\d+?)\,', string)
    return items


def get_sheet_data(excel_path, sheet_name, idx, column_key, column_value, is_parser=True):
    """
    公共方法
    获取指定excel中的指定sheet表中的指定列的数据
    """
    wb = ExcelTool(excel_path)
    ws = wb.get_sheet(sheet_name)
    ws_rows_max = ws.max_row
    idx = idx
    items = {}
    while idx <= ws_rows_max:
        item_key = ws.cell(row=idx, column=column_key).value
        item_value = ws.cell(row=idx, column=column_value).value
        if is_parser:
            items.update({item_key: parser_string(item_value)})
        else:
            items.update({item_key: item_value})
        idx += 1
    return items


def mapping_ident_dict(mapping_data, target_data):

    mapping_dict = {}
    for level_name, items_id in mapping_data.items():
        items_list = []
        for item_id in items_id:
            if int(item_id) == 1:
                items_list.append('金币')
            if int(item_id) == 5:
                items_list.append('钻石')
            for ident_id, reward_name in target_data.items():
                if str(ident_id) == str(item_id):
                    items_list.append(reward_name)

        mapping_dict.update({level_name: items_list})
    return mapping_dict


def get_row_shadow_data():
    wb = ExcelTool(dungeon_path)
    ws = wb.get_sheet('CfgDungeonLevel')

    wb2 = ExcelTool(mapping_path)
    ws2 = wb2.get_sheet('虚影殿堂')

    start_idx = 85
    end_idx = 173
    item = {}
    while start_idx <= end_idx:
        item_key = ws.cell(row=start_idx, column=3).value
        item_value = ws.cell(row=start_idx, column=15).value
        start_idx += 1
        if '废弃' in str(item_key):
            continue
        item.update({item_key: item_value})

    idx = 2
    for key, value in item.items():
        ws2.cell(row=idx, column=1).value = key
        ws2.cell(row=idx, column=6).value = value
        idx += 1

    wb2.workbook.save(mapping_path)

    return item


def mapping_shadow_drop_item(item: dict):
    wb = ExcelTool(drop_bag_path)
    ws = wb.get_sheet('掉落母表')
    start_idx = 1650
    end_idx = 1739
    items2 = {}
    while start_idx <= end_idx:
        item_key = ws.cell(row=start_idx, column=2).value
        item_value = ws.cell(row=start_idx, column=7).value
        for key, value in item.items():
            if str(value) == str(item_key):
                items2.update({key: item_value})
        start_idx += 1

    wb2 = ExcelTool(mapping_path)
    ws2 = wb2.get_sheet('虚影殿堂')
    idx = 2
    for k, v in items2.items():
        ws2.cell(row=idx, column=5).value = v
        idx += 1

    wb2.workbook.save(mapping_path)
    return items2


def write_data(mapping_dict, sheet_name,  column=8, idx=2):
    items_list = [i for i in mapping_dict.values()]
    wb = ExcelTool(mapping_path)
    ws = wb.get_sheet(sheet_name)
    ws_rows_max = ws.max_row
    while idx <= ws_rows_max:
        ws.cell(row=idx, column=column).value = str(items_list[idx-2])
        idx += 1
    wb.workbook.save(mapping_path)


def write_shadow_data():
    # item1 = get_row_shadow_data()
    # mapping_shadow_drop_item(item1)
    sheet_name = '虚影殿堂'
    mapping_data = get_sheet_data(mapping_path, sheet_name, 2, 1, 5, True)
    target_data = get_sheet_data(item_path, 'CfgItem', 4, 2, 3, False)
    mapping_dict = mapping_ident_dict(mapping_data, target_data)
    write_data(mapping_dict, sheet_name)


def write_forbid_data():
    sheet_name = '贪婪禁地'
    mapping_data = get_sheet_data(mapping_path, sheet_name, 2, 1, 5, True)
    target_data = get_sheet_data(item_path, 'CfgItem', 4, 2, 3, False)
    mapping_dict = mapping_ident_dict(mapping_data, target_data)
    write_data(mapping_dict, sheet_name)


def write_sky_data():
    sheet_name = '苍穹之城'
    mapping_data = get_sheet_data(mapping_path, sheet_name, 2, 1, 5, True)
    target_data = get_sheet_data(item_path, 'CfgItem', 4, 2, 4, False)
    mapping_dict = mapping_ident_dict(mapping_data, target_data)
    language_data = get_sheet_data(language_path, 'CfgLanItem', 4, 2, 4, False)

    dic_ = {}
    for k, v in mapping_dict.items():
        for j in v:
            for i, o in language_data.items():
                if str(i) == str(j):
                    v.remove(j)
                    v.append(o)
        dic_.update({k: v})

    dic_2 = {}
    for k, v in mapping_dict.items():
        for j in v:
            for i, o in language_data.items():
                if str(i) == str(j):
                    v.remove(j)
                    v.append(o)
        dic_2.update({k: v})

    write_data(dic_2, sheet_name)


if __name__ == '__main__':
    # item = get_row_shadow_data()
    # mapping_shadow_drop_item(item)
    write_shadow_data()
