from tests.page.profile import ProfilePage, log
from tests.position.profile_pos import *
from tests.lib.utils import assertion


class ProfileProxy:

    def __init__(self, poco_instance):
        self.profile = ProfilePage(poco_instance)

    def verify_rename(self):
        self.profile.open_avatar_menu()
        self.profile.rename()
        self.profile.input_nickname()
        self.profile.confirm()
        self.profile.confirm()
        self.profile.tap_anywhere()

    def verify_edit_signature(self):
        self.profile.open_avatar_menu()
        self.profile.edit_signature()
        self.profile.input_signature()
        self.profile.confirm()
        self.profile.tap_anywhere()

    def verify_edit_avatar(self):
        self.profile.open_avatar_menu()
        self.profile.edit_avatar()
        self.profile.choose_avatar()
        self.profile.apply_btn()
        self.profile.close_btn()
        self.profile.tap_anywhere()



