# @Time   : 2022/11/11 10:37
# @Author : LOUIE
# @Desc   : GM命令调用工具类

import requests
import setting
from utils import logstep


def _execute_command(cmd):
    """
    执行GM命令，执行前必须配置好GM_COOKIE
    :param cmd:
    :return:
    """
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Cookie": setting.GM_COOKIE
    }
    data = {
        "id": 0,
        "server_type": "test",
        "server_id": setting.GM_SERVER_ID,
        "exec_type": 1,
        "platform_id": setting.GM_PLATFORM_ID,
        "game_id": 9,
        "action": "save",
        "command": cmd,
        "csv_file": ""
    }
    res = requests.post(url=setting.GM_URL, data=data, headers=headers)
    res.raise_for_status()
    res = res.json()
    if res['code'] != 0:
        raise requests.exceptions.HTTPError(res['msg'])
    logstep(f'Run the GM command : {cmd}')
    return res


def clear_hero(pid: int):
    """
    清空英雄
    :param pid: 玩家编号
    :return:
    """
    cmd = f'clearHero {pid}'
    return _execute_command(cmd)


def clear_item(pid: int):
    """
    清空道具
    :param pid: 玩家编号
    :return:
    """
    cmd = f'clearItem {pid}'
    return _execute_command(cmd)


def complete_activity(pid: int, activity_id: int, reward_id: int, count: int):
    """
    完成活动进度
    :param pid: 玩家编号
    :param activity_id: 活动ID
    :param reward_id: 奖励ID
    :param count:
    :return:
    """

    cmd = f'addActivityProgress {pid} {activity_id} {reward_id} {count}'
    return _execute_command(cmd)


def complete_target_task(pid: int, task_id: int, count: int):
    """
    完成指定活动进度
    :param pid: 玩家编号
    :param task_id: 任务ID
    :param count:
    :return:
    """

    cmd = f'addTaskProgress {pid} {task_id} {count}'
    return _execute_command(cmd)


def set_main_task(pid: int, chapter: int, plot_id: int):
    """
    重置主线剧情到指定的剧情
    :param pid: 玩家编号
    :param chapter: 章节ID
    :param plot_id: 剧情ID
    :return:
    """

    cmd = f'setMainTask {pid} {chapter} {plot_id}'
    return _execute_command(cmd)


def set_dungeon_progress(pid: int, level_type: int, chapter_index: int, level_count: int):
    """
    重置关卡到指定关卡(用完gm命令需要重新登录)
    :param pid: 玩家编号
    :param level_type: 关卡类型: 1.普通 2.精英
    :param chapter_index: 章节索引
    :param level_count: 通关关卡数量
    :return:
        example: setDungeonProgress 95756 1 11 6
    """

    if level_type not in [1, 2]:
        return
    cmd = f'setDungeonProgress {pid} {level_type} {chapter_index} {level_count}'
    return _execute_command(cmd)


def set_hero_star(pid: int, count: int):
    """
    设置英雄星级
    :param pid: 玩家编号
    :param count: 星级数量
    :return:
    """

    cmd = f'batchSetHeroAttr {pid} 505 {count}'
    return _execute_command(cmd)


def set_hero_up(pid: int, count: int):
    """
    设置英雄进阶
    :param pid: 玩家编号
    :param count: 进阶数量
    :return:
    """

    cmd = f'batchSetHeroAttr {pid} 502 {count}'
    return _execute_command(cmd)


def set_hero_level(pid: int, count: int):
    """
    设置英雄等级
    :param pid: 玩家编号
    :param count: 等级数量
    :return:
    """

    cmd = f'batchSetHeroAttr {pid} 501 {count}'
    return _execute_command(cmd)


def clear_player(pid):
    """
    清除账号信息
    :param pid: 玩家编号
    :return:
    """

    cmd = f'clearPlayer {pid}'
    return _execute_command(cmd)


def set_server_time(pid: int, time_fmt: str):
    """
    设置服务器时间
    :param pid: 玩家编号
    :param time_fmt: 时间日期字符串
    :return:
    """

    # 对时间日期字符串进行判断是否为指定格式
    if time_fmt:
        pass
    year, month, day, hour, minute, second = time_fmt
    cmd = f'setServerTime {pid} {year} {month} {day} {hour} {minute} {second}'
    return _execute_command(cmd)


def add_value(pid: int, res_type: int, count: int):
    """
    增加资源
    :param pid: 玩家编号
    :param res_type: 声望类型
    :param count: 声望值
    :return:
    """

    cmd = f'addValue {pid} 1009 {res_type} {count}'
    return _execute_command(cmd)


def add_res(pid: int, res_type: int, point: int):
    """
    添加普通资源
    :param pid: 玩家编号
    :param res_type: 声望类型
    :param point: 声望值
    :return:
    """

    cmd = f'addRes {pid} {res_type} {point}'
    return _execute_command(cmd)


def add_hero(pid: int, hero_type: int = 199999, count: int = 1):
    """
    添加资源命令
    :param pid: 玩家编号: 我的编号 55561040
    :param hero_type: 英雄类型 : 199999 - 秒杀英雄
    :param count: 数量
    :return:
    """

    cmd = f'addHero {pid} {hero_type} {count}'
    return _execute_command(cmd)


def add_item(pid: int, res_type: int, point: int):
    """
    添加资源命令
    :param pid: 玩家编号
    :param res_type: 声望类型
    :param point: 声望值
    :return:
    """

    cmd = f'addItem {pid} {res_type} {point}'
    return _execute_command(cmd)


def refresh_opponent(pid: int, opponent_id: int):
    """
    添加资源命令
    :param pid: 玩家编号
    :param opponent_id: 对手ID
    :return:
    """

    cmd = f'refreshOpponent {pid} {opponent_id}'
    return _execute_command(cmd)


def set_arena_score(pid: int, score: int):
    """
    设置竞技场积分
    :param pid: 玩家编号
    :param score: 积分数
    :return:
    """

    cmd = f'setArenaScore {pid} {score}'
    return _execute_command(cmd)


def buy_gift_bag(pid: int, score: int):
    """
    购买礼包
    :param pid: 玩家编号
    :param score: 积分数
    :return:
    """

    cmd = f'buyGiftBag {pid} {score}'
    return _execute_command(cmd)


def run_batch_cmd(pid, cmd):
    """
    通关主线等等...
    :param pid: 玩家编号
    :param cmd: 命令: 666666 777777 888888 999999
    :return:
    """

    cmd = f'runBatchCmd {pid} {cmd}'
    return _execute_command(cmd)


class Player:

    def __init__(self, pid):
        self.pid = pid

    @staticmethod
    def execute_command(cmd):
        """添加能量"""
        return _execute_command(cmd)

    def add_hero_level(self, count=100000):
        """提升人物等级"""
        return add_res(self.pid, 101, count)

    def add_energy(self, count=1000):
        """添加能量"""
        return add_value(self.pid, 10011, count)

    def add_coins(self, count=5000):
        """添加金币"""
        return add_value(self.pid, 10011, count)

    def add_jewel(self, count=5000):
        """添加钻石"""
        return add_value(self.pid, 10011, count)

    def add_hero(self, count=1):
        """添加英雄"""
        return add_hero(self.pid, 199999, count)

    def add_gold_key(self, count=999):
        """添加黄金谷金钥"""
        return add_value(self.pid, 10021, count)

    def clear_player(self):
        """添加英雄"""
        return clear_player(self.pid)

    def clear_item(self):
        """清理道具"""
        return clear_item(self.pid)

    def run_batch_cmd(self, cmd=666666):
        """通过主线"""
        return run_batch_cmd(self.pid, cmd)

    def set_main_task(self, chapter: int, plot_id: int):
        """通过主线任务"""
        return set_main_task(self.pid, chapter, plot_id)

    def set_dungeon_progress(self, level_type: int, chapter_index: int, level_count: int):
        """
        重置关卡到指定关卡(用完gm命令需要重新登录)
        """
        return set_dungeon_progress(self.pid, level_type, chapter_index, level_count)


if __name__ == '__main__':
    player_id = 55679568
    player1 = Player(pid=player_id)
    # player1.clear_player()
    # player1.add_energy()
    # player1.add_hero_level(-500000)
    # player1.run_batch_cmd()
    # 1. 通关所有的关卡 2. 添加超级英雄 3. 清理背包
    # player1.add_hero()
    player1.set_main_task(11012, 14120460)
    # player1.set_dungeon_progress(1, 11, 18)
    # player1.add_gold_key()


