# @Time   : 2022/11/10 16:07
# @Author : LOUIE
# @Desc   : to do something ...
import random


# 体力、金币、钻石、购买能量、购买金币
strength_pos = 'resContainer/ResourceContainer(Clone)/ResComponent(Clone)[0]'
coin_pos = 'resContainer/ResourceContainer(Clone)/ResComponent(Clone)[1]'
jewel_pos = 'resContainer/ResourceContainer(Clone)/ResComponent(Clone)[2]'
buy_strength_pos = 'topList/resContainer/ResourceContainer(Clone)/ResComponent(Clone)/Add_btn_click'
buy_coin_pos = 'topList/resContainer/ResourceContainer(Clone)/ResComponent(Clone)'

# 个人信息：改名按钮、改签名按钮、昵称输入框、确定按钮
rename_btn_pos = 'Btn_change_01[0]'
edit_signature_btn_pos = 'Btn_change_01[1]'
inputField_pos = 'InputField'
confirm_btn_pos = 'YellowButton02'

# 编辑头像按钮、头像栏、头像框栏、名片栏
edit_avatar_btn_pos = 'AvatarComponentLarge(Clone)'
avatar_item_pos = 'textMatches=头像'
avatar_frame_item_pos = 'textMatches=头像框'
business_card_item_pos = 'textMatches=名片'
choose_avatar_pos = f'nameMatches=AvatarContainer[{random.randint(0, 8)}]'
apply_btn_pos = 'BtnApply'
close_btn_pos = 'CloseBtn'


prompt_text_pos = 'TextLabel0'

# 删除已读、一键已读
delete_read_pos = 'BlueButton02'
read_all_pos = 'YellowButton02'
close_mail_pos = 'Popclose_01_bg'








