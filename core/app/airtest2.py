from airtest.core import api


def init_device(platform=None, uuid=None, **kwargs):
    api.init_device(platform=platform, uuid=uuid, **kwargs)


def connect_device(uri):
    api.connect_device(uri)


def device():
    return api.device()


def set_current(idx):
    api.set_current(idx)


def auto_setup(basedir=None, devices=None, logdir=None, project_root=None, compress=None):
    api.auto_setup(basedir=basedir, devices=devices, logdir=logdir, project_root=project_root, compress=compress)


def shell(cmd):
    return api.shell(cmd)


def start_app(package, activity=None):
    api.start_app(package, activity)


def stop_app(package):
    api.start_app(package)
















