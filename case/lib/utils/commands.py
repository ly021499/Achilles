# @Time   : 2022/11/11 10:37
# @Author : LOUIE
# @Desc   : GM命令调用

import requests
import setting


def execute_command(cmd):
    url = setting.GM_URL
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": setting.GM_COOKIE
    }
    data = {
        "id": 0,
        "server_type": "test",
        "server_id": 80000337,
        "exec_type": 1,
        "platform_id": 80,
        "game_id": 9,
        "action": "save",
        "command": cmd,
        "csv_file": ""
    }
    return requests.post(url=url, data=data, headers=headers)


def complete_activity(pid: int, activity_id: int, reward_id: int, count: int):
    """
    完成活动进度
    :param pid:
    :param activity_id: 活动ID
    :param reward_id: 奖励ID
    :param count:
    :return:
    """

    cmd = f'addActivityProgress {pid} {activity_id} {reward_id} {count}'
    execute_command(cmd)


def complete_target_task(pid: int, task_id: int, count: int):
    """
    完成指定活动进度
    :param pid:
    :param task_id: 任务ID
    :param count:
    :return:
    """

    cmd = f'addTaskProgress {pid} {task_id} {count}'
    execute_command(cmd)


def set_main_task(pid: int, plot_id: int):
    """
    重置主线剧情到指定的剧情
    :param pid:
    :param plot_id: 剧情ID
    :return:
    """

    cmd = f'setMainTask {pid} {plot_id}'
    execute_command(cmd)


def set_dungeon_progress(pid: int, level_type: int, chapter_index: int, level_count: int):
    """
    重置关卡到指定关卡(用完gm命令需要重新登录)
    :param pid:
    :param level_type: 关卡类型: 1.普通 2.精英
    :param chapter_index: 章节索引
    :param level_count: 通关关卡数量
    :return:
        example: setDungeonProgress 95756 1 11 6
    """

    if level_type not in [1, 2]:
        return
    cmd = f'setDungeonProgress {pid} {level_type} {chapter_index} {level_count}'
    execute_command(cmd)


def set_hero_star(pid: int, count: int):
    """
    设置英雄星级
    :param pid:
    :param count: 星级数量
    :return:
    """

    cmd = f'batchSetHeroAttr {pid} 505 {count}'
    execute_command(cmd)


def set_hero_up(pid: int, count: int):
    """
    设置英雄进阶
    :param pid:
    :param count: 进阶数量
    :return:
    """

    cmd = f'batchSetHeroAttr {pid} 502 {count}'
    execute_command(cmd)


def set_hero_level(pid: int, count: int):
    """
    设置英雄等级
    :param pid:
    :param count: 等级数量
    :return:
    """

    cmd = f'batchSetHeroAttr {pid} 501 {count}'
    execute_command(cmd)


def clear_player(pid: int):
    """
    清除账号信息
    :param pid:
    :return:
    """

    cmd = f'batchSetHeroAttr {pid}'
    execute_command(cmd)


def set_server_time(pid: int, time_fmt: str):
    """
    设置服务器时间
    :param pid:
    :param time_fmt: 时间日期字符串
    :return:
    """

    # 对时间日期字符串进行判断是否为指定格式
    if time_fmt:
        pass
    year, month, day, hour, minute, second = time_fmt
    cmd = f'setServerTime {pid} {year} {month} {day} {hour} {minute} {second}'
    execute_command(cmd)


def add_res(pid: int, res_type: int, point: int):
    """
    添加资源命令
    :param pid:
    :param res_type: 声望类型
    :param point: 声望值
    :return:
    """

    cmd = f'addRes {pid} {res_type} {point}'
    execute_command(cmd)


def refresh_opponent(pid: int, opponent_id: int):
    """
    添加资源命令
    :param pid:
    :param opponent_id: 对手ID
    :return:
    """

    cmd = f'refreshOpponent {pid} {opponent_id}'
    execute_command(cmd)


def set_arena_score(pid: int, score: int):
    """
    设置竞技场积分
    :param pid:
    :param score: 积分数
    :return:
    """

    cmd = f'setArenaScore {pid} {score}'
    execute_command(cmd)

