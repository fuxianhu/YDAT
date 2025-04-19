
# 尝试导入 logging 模块、设置格式和日志文件

import logging

# 对logger进行配置——日志等级&输出格式
try:
    logging.basicConfig(level=logging.DEBUG, format="(%(asctime)s) [%(levelname)s] %(message)s", filename="./log/ydat.log")
except FileNotFoundError as err:
    raise FileNotFoundError(f"{err}")


# 尝试导入需要的模块

try:
    from pyautogui import *
    from tkinter import *
    from tkinter.ttk import *
    from tkinter.messagebox import *
    from tkinter.filedialog import *
    from tkinter.simpledialog import *
    from tkinter.colorchooser import *
    import time
    import os
    import sys
    import threading
    import subprocess
    import webbrowser
    import platform
except ModuleNotFoundError as err:
    logging.log(f"{err}", level=logging.CRITICAL)
    raise ModuleNotFoundError(f"{err}")


# 判断当前操作系统的平台表示
# 常见的返回值包括：
# 'linux'：Linux系统
# 'win32'：Windows系统
# 'darwin'：macOS系统
os_name = platform.system()
if os_name == 'Linux':
    raise OSError("Ydat不支持Linux平台，请使用Windows操作系统。")
elif os_name == 'Darwin':
    raise OSError("Ydat不支持macOS平台，请使用Windows操作系统。")
elif os_name != 'Windows':
    logging.log(f"Ydat对此平台的兼容性未知，请谨慎使用！", level=logging.WARNING)
    # raise OSError("Ydat不支持此平台，请使用Windows操作系统。")
else:
    logging.log("平台 Windows", level=logging.DEBUG)


