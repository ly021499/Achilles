# @Time   : 2022/11/2 21:05
# @Author : LOUIE
# @Desc   : 解析excel数据
from utils.match import match_string
from openpyxl import load_workbook
from utils.excel_tool import ExcelTool
import time
import os
import setting


EXCEL_DIR = 'D:\\MainTrunk\\Excels\\Dev'                       # EXCEL存放基础目录
mapping_path = os.path.join(setting.RES_DIR, 'excel\\mapping.xlsx') # 终端映射表
drop_path = os.path.join(EXCEL_DIR, 'CfgDropBag.xlsx')     # 掉落包表
equipment_path = os.path.join(EXCEL_DIR, 'CfgEquipment.xlsx')  # 装备表
language_path = os.path.join(EXCEL_DIR, 'CfgLanguage.xlsx')    # 语言匹配表
item_path = os.path.join(EXCEL_DIR, 'CfgItem.xlsx')            # 物品表
dungeon_path = os.path.join(EXCEL_DIR, 'CfgDungeon.xlsx')      # 地牢表（我也不知道是啥）

class Mapping():

    def __init__(self):
        self.et = ExcelTool(mapping_path)
        self.mapping_data = None

    def get_first_reward(self, sheet):
        """
        获取首次掉落奖励
        """
        sheet_list = ['茫然遗迹', '元素峡谷']
        if sheet not in sheet_list:
            raise ModuleNotFoundError(f"sheet '{sheet}' not in list {sheet_list} .")
        self.et.get_sheet(sheet)
        return self.et.get_parser_col_list(col=5, start_row=2, end_row=self.et.get_max_row())

    def get_regular_reward(self, sheet):
        """
        获取常规掉落奖励
        """
        sheet_list = ['茫然遗迹', '元素峡谷', '贪婪禁地', '虚影殿堂', '苍穹之城']
        if sheet not in sheet_list:
            raise ModuleNotFoundError(f"sheet '{sheet}' not in list {sheet_list} .")
        self.et.get_sheet(sheet)
        return self.et.get_parser_col_list(col=2, start_row=2, end_row=self.et.get_max_row())


class Parser():

    def get_target_data(self, filepath, sheet, col_key, col_var, start_row=2, end_row=None):
        """
        获取指定数据
        """
        et = ExcelTool(filepath)
        et.get_sheet(sheet)
        return et.get_col_dict(col_key, col_var, start_row, end_row)

    def get_mapping_data(self, mapping_items: list, mapping_data: dict):
        """
        公用匹配数据方法
        """
        if not isinstance(mapping_data, dict):
            raise TypeError('mapping data need to be a dict')
        mapping = []
        for mapping_item in mapping_items:
            item = mapping_data.get(mapping_item)
            if item is not None:
                mapping.append(item)
            else:
                mapping.append(None)
        return mapping

    def mapping_equipment(self, mapping_items):
        """
        映射装备标识符
        """
        equipment = self.get_target_data(equipment_path, 'CfgEquipment', 2, 8, 2, is_parser_value=False)
        return self.get_mapping_data(mapping_items, equipment)

    def mapping_chinese_name(self, equipment):
        """
        映射中文名称
        """
        language = self.get_target_data(language_path, 'CfgLanSystem', 2, 8, 2, is_parser_value=False)
        return self.get_mapping_data(equipment, language)


class Busy():

    def __init__(self):
        self.et = ExcelTool(mapping_path)

    def write_mapping_data(self):
        self.et.write_data(mapping_path)

    def write_assert_result(self):
        """
        写入断言结果数据
        """

    def write_shadow_to_mapping(self):
        """
        查找 虚影宫殿 的原始表数据并写入新的 mapping.xlsx 表中
        """

    def write_element_to_mapping(self):
        """
        查找虚 元素峡谷 的原始表数据并写入新的 mapping.xlsx 表中
        """

    def write_sky_to_mapping(self):
        """
        查找虚 苍穹之城 的原始表数据并写入新的 mapping.xlsx 表中
        """

    def write_forbid_to_mapping(self):
        """
        查找虚 贪婪禁地 的原始表数据并写入新的 mapping.xlsx 表中
        """

    def write_lost_to_mapping(self):
        """
        查找虚 茫然遗迹 的原始表数据并写入新的 mapping.xlsx 表中
        """

    def init_mapping_data(self):
        self.write_element_to_mapping()
        self.write_lost_to_mapping()
        self.write_forbid_to_mapping()
        self.write_shadow_to_mapping()
        self.write_sky_to_mapping()

    def init_reward_data(self):
        start_time = time.time()

        end_time = time.time()
        duration = round(end_time - start_time, 2)
        print('duration: ', duration)

