# @Time   : 2022/11/16 16:02
# @Author : LOUIE
# @Desc   : 验证能量、金钥消耗正确

from tests.lib.driver.unity_app import Unity3dPocoUnit
from tests.proxy.profile import ProfileProxy
from utils import log


class Test_Modify_profile(Unity3dPocoUnit):

    def setUp(self) -> None:
        self.profile = ProfileProxy(self.poco)

    @log.case
    def test_a_rename(self):
        self.profile.verify_rename()

    @log.case
    def test_b_edit_avatar(self):
        self.profile.verify_edit_avatar()

    @log.case
    def test_c_edit_signature(self):
        self.profile.verify_edit_signature()
