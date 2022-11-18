# @Time   : 2022/11/17 18:28
# @Author : LOUIE
# @Desc   : to do something ...
from poco.drivers.unity3d import UnityPoco
from poco.drivers.unity3d.device import UnityEditorWindow


def get_unity_window_poco_instance():
    dev = UnityEditorWindow()
    addr = ('', 5001)

    return UnityPoco(addr, device=dev)


