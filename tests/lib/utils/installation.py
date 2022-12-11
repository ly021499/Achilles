from airtest.utils.apkparser.apk import APK
import re


def install_android_app(adb_client, local_path, force_reinstall=False):
    apk_info = APK(local_path)
    package_name = apk_info.package

    def _get_installed_apk_version(package):
        package_info = adb_client.shell(['dumpsys', 'package', package])
        matcher = re.search(r'versionCode=(\d+)', package_info)
        if matcher:
            return int(matcher.group(1))
        return None

    try:
        apk_version = int(apk_info.androidversion_code)
    except (RuntimeError, ValueError):
        apk_version = 0
    installed_version = _get_installed_apk_version(package_name)

    print(f'installed version is {installed_version}, '
          f'installer version is {apk_version}. '
          f'force_reinstall={force_reinstall}')

    if installed_version is None or apk_version > installed_version or force_reinstall:
        if installed_version is not None:
            force_reinstall = True
        if hasattr(adb_client, 'install_app'):
            adb_client.install_app(local_path, force_reinstall)
        else:
            adb_client.install(local_path, force_reinstall)
        return True
    return False


def uninstall_android_app(adb_client, package):
    if hasattr(adb_client, 'uninstall_app'):
        adb_client.uninstall_app(package)
    else:
        adb_client.uninstall(package)
