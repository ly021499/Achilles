from poco.drivers.unity3d import UnityPoco
from poco.drivers.unity3d.device import UnityEditorWindow

dev = UnityEditorWindow()

addr = ('', 5001)

poco = UnityPoco(addr, device=dev)

ui = poco('Mainmail_btn')
ui.click()
