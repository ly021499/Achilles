from poco.drivers.unity3d import UnityPoco
from poco.drivers.unity3d.device import UnityEditorWindow
from case.page.profile import ProfilePage

# specify to work on UnityEditor in this way
dev = UnityEditorWindow()

addr = ('', 5001)

# 指定设备对象初始化unity poco
poco = UnityPoco(addr, device=dev)

page = ProfilePage(poco)
page.click_strength()
